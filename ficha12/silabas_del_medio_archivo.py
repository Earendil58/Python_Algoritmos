import os

def obtenerTexto(archivo):
    cadena = ''

    if not os.path.exists(archivo):
        print(f'El archivo: {archivo} no existe')
        return cadena

    with open(archivo, 'r', encoding='utf-8') as texto:
        cadena = texto.read()

    return cadena



def caracterDigito(caracter):
    digitos = '123456789'
    if caracter in digitos:
        return True
    return False



def contadorPalabrasConDigito(booleanReturn):
    palabras_con_digitos = 0
    if booleanReturn:
        palabras_con_digitos += 1

    return palabras_con_digitos

def principal():
    texto_a_analizar = obtenerTexto('./silabas_de_primera_mitad.txt')
    print(f'El texto es: {texto_a_analizar}')

    cant_letras = 0
    cant_palabras_con_digitos = 0
    ya_salio_digito = False
    cant_palabras_en_Texto = 0
    palabras_hasta_tres_letras = palabras_entre_cuatro_seis_letras = palabras_mas_seis_letras = 0

    for caracter in texto_a_analizar:

        if caracter == ' ' or caracter == '.':
            cant_palabras_en_Texto += 1
            ya_salio_digito = False

            if cant_letras <= 3:
                palabras_hasta_tres_letras += 1

            elif 4 <= cant_letras <= 6:
                palabras_entre_cuatro_seis_letras += 1

            elif cant_letras > 6:
                palabras_mas_seis_letras += 1

            cant_letras = 0

        else:
            cant_letras += 1
            if caracterDigito(caracter) and ya_salio_digito == False:
                cant_palabras_con_digitos += 1
                ya_salio_digito = True

    #RESPUESTAS otras
    print(f'La cantidad de palabras con dígitos en el texto son: {cant_palabras_con_digitos}', end='\n')
    print(f'La cantidad de palabras que tienen hasta 3 letras son: {palabras_hasta_tres_letras}')
    print(f'La cantidad de palabras que tienen entre 4 y 6 letras son: {palabras_entre_cuatro_seis_letras}')
    print(f'La cantidad de palabras que tienen más de 6 letras son: {palabras_mas_seis_letras}')



principal()