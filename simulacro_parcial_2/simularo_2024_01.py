def es_letra(caracter):
    return 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z'

def es_letra_minuscula(caracter):
    return 'a' <= caracter <= 'z'

def es_vocal(caracter):
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    return caracter in vocales

def es_consonante(caracter):
    return es_letra(caracter) and not es_vocal(caracter)

def es_numero(caracter):
    return '0' <= caracter <= '9'

def es_impar(caracter):
    return int(caracter) % 2 != 0

def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio




def principal():
    tratar_archivo = open('./simulacro_2024_01.txt', 'rt')
    texto = tratar_archivo.read()
    tratar_archivo.close()

    print(texto)

    cant_palabras_comienzan_digito_siguen_letras_minusculas = 0
    cant_caracter_por_palabra = 0
    primer_caracter_digito = False
    letras_minusculas_dsp_de_caracter_numerico = True
    longitud_palabra_mas_larga = 0
    comienza_vocal = False
    contiene_b = False
    cant_letras_consonantes = 0
    cant_palabras_consonantes = 0
    cant_vocales = 0
    cant_consonantes = 0
    tiene_m = tiene_a = False


    for letra in texto:
        if letra == ' ' or letra == '.':

            if primer_caracter_digito and letras_minusculas_dsp_de_caracter_numerico:
                cant_palabras_comienzan_digito_siguen_letras_minusculas += 1

            elif comienza_vocal and contiene_b:
                if longitud_palabra_mas_larga == 0:
                    longitud_palabra_mas_larga = cant_caracter_por_palabra
                else:
                    if cant_caracter_por_palabra > longitud_palabra_mas_larga:
                        longitud_palabra_mas_larga = cant_caracter_por_palabra

            if cant_consonantes > cant_vocales and not tiene_a and not tiene_m:
                cant_letras_consonantes += cant_caracter_por_palabra
                cant_palabras_consonantes += 1



            cant_caracter_por_palabra = 0
            primer_caracter_digito = False # R1 FLAGS
            letras_minusculas_dsp_de_caracter_numerico = True  # R1 FLAGS
            comienza_vocal = contiene_b = False  # R2 FLAGS
            cant_consonantes = cant_vocales = 0  # R3 FLAGS
            tiene_a = tiene_m = False # R3 FLAGS



        else:
            cant_caracter_por_palabra += 1

            if cant_caracter_por_palabra == 1:
                if es_numero(letra) and es_impar(letra):
                    primer_caracter_digito = True

                elif es_vocal(letra):
                    comienza_vocal = True

            elif cant_caracter_por_palabra > 1:
                if not(es_letra_minuscula(letra)):
                    letras_minusculas_dsp_de_caracter_numerico = False

                elif letra == 'b':
                    contiene_b = True

            if es_vocal(letra):
                cant_vocales += 1
                if letra == 'a' or letra == 'A':
                    tiene_a = True


            if es_consonante(letra):
                cant_consonantes += 1
                if letra == 'm' or letra == 'M':
                    tiene_m = True





    r1 = cant_palabras_comienzan_digito_siguen_letras_minusculas
    r2 = longitud_palabra_mas_larga
    r3 = calcular_promedio(cant_letras_consonantes, cant_palabras_consonantes)




    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)




if __name__ == '__main__':
    principal()


