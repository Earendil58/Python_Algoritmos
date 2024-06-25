def es_letra(caracter):
    return 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z'

def es_letra_minuscula(caracter):
    return 'a' <= caracter <= 'z'


def es_numero(letra):
    return '0' <= letra <= '9'





def principal():
    tratar_archivo = open('./simulacro_2024_01.txt', 'rt')
    texto = tratar_archivo.read()
    tratar_archivo.close()

    print(texto)

    cant_palabras_comienzan_digito_siguen_letras_minusculas = 0
    cant_caracter_por_palabra = 0
    primer_caracter_digito = False
    letras_minusculas_dsp_de_caracter_numerico = True


    for letra in texto:
        if letra == ' ' or letra == '.':

            if letras_minusculas_dsp_de_caracter_numerico:
                cant_palabras_comienzan_digito_siguen_letras_minusculas += 1

            cant_caracter_por_palabra = 0
            primer_caracter_digito = False
            letras_minusculas_dsp_de_caracter_numerico = True


        else:
            cant_caracter_por_palabra += 1

            if cant_caracter_por_palabra == 1 and es_numero(letra):
                primer_caracter_digito = True

            if primer_caracter_digito and not(es_letra_minuscula(letra)):
                letras_minusculas_dsp_de_caracter_numerico = False



        r1 = cant_palabras_comienzan_digito_siguen_letras_minusculas
            



    print("Primer resultado:", r1)
    # print("Segundo resultado:", r2)
    # print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)




if __name__ == '__main__':
    principal()

