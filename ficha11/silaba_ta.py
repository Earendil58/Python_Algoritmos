# El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La frase finaliza con un punto, y las palabras están separadas por espacios únicamente.
# Se debe mostrar:
#
# a) Ver el porcentaje de vocales respecto del total de letras de la frase.
#
# b) La longitud promedio de las palabras
#
# c) La longitud de la palabra mas larga del texto
#
# d) Cantidad de palabras que comienzan con "ta"


def analizarTexto():
    #DATOS
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    cant_vocales = 0
    cant_letras_totales = 0
    longitud_palabra_mas_larga_texto = None
    cant_palabras_ta = 0
    cant_palabras_texto = 0
    contador_caracter = 0
    longitud_palabra = 0
    hay_t = False
    hay_a = False

    texto = input('Ingrese su texto: ')
    texto = texto.strip()
    texto = texto.lower()

    while len(texto) <= 0:
        texto = input('Ingrese su texto: ')
        texto = texto.strip()
        texto = texto.lower()

    for letra in texto:

        if letra != ' ':
            contador_caracter += 1

        if letra == ' ' or letra == '.':
            if contador_caracter > 0:
                cant_palabras_texto += 1
                longitud_palabra += contador_caracter
                if longitud_palabra_mas_larga_texto == None:
                    longitud_palabra_mas_larga_texto = contador_caracter
                else:
                    if contador_caracter > longitud_palabra_mas_larga_texto:
                        longitud_palabra_mas_larga_texto = contador_caracter

                if hay_t and hay_a:
                    cant_palabras_ta += 1
                hay_t = False
                hay_a = False

            contador_caracter = 0



        else:
            cant_letras_totales += 1
            if letra in vocales:
                cant_vocales += 1

            if contador_caracter == 1 and letra == 't':
                hay_t = True
            if contador_caracter == 2 and letra == 'a':
                hay_a = True



        anterior = letra


    porcentaje_vocales_sobre_total_letras_texto = round((cant_vocales * 100) / cant_letras_totales, 2)
    longitud_promedio_palabras = round(longitud_palabra / cant_palabras_texto, 2)

    print(f'El porcentaje de vocales sobre el total de letras en el texto, es de: {porcentaje_vocales_sobre_total_letras_texto}%')
    print(f'La longitud promedio de las palabras en el texto fue de: {longitud_promedio_palabras}')
    print(f'La palabra más larga en el texto tiene una longitud de: {longitud_palabra_mas_larga_texto}')
    print(f'La cantidad de palabras que comienzan con "ta" es: {cant_palabras_ta}')


analizarTexto()

