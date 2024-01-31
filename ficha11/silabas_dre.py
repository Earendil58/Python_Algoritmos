# Desarrollar un programa en Python que permita cargar por teclado un texto completo.
# Siempre se supone que el usuario cargará un punto para indicar el final del texto,
# y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
#
# a) Determinar cuántas palabras tenían exactamente 3 letras.
#
# b) Determinar el porcentaje que las palabras del punto 1 representan en el total del palabras del texto.
#
# c) Determinar cuántas palabras terminaban con la letra "s".
#
# d) Determinar cuántas palabras contuvieron al menos una vez la expresión "dre".

def analizarTexto():

    texto = input('Ingrese el texto a analizar: ')
    texto = texto.lower()

    cant_palabras_3_letras = 0
    cant_palabras_totales = 0
    cant_palabras_terminan_s = 0
    cant_palabras_que_tienen_al_menos_una_vez_dre = 0
    anterior = None
    contador_caracter = 0
    tiene_d = False
    tiene_dr = False
    tiene_dre = False

    for letra in texto:

        if letra == ' ' or letra == '.':
            cant_palabras_totales += 1
            if contador_caracter == 3:
                cant_palabras_3_letras += 1

            if anterior == 's':
                cant_palabras_terminan_s += 1

            if tiene_dre:
                cant_palabras_que_tienen_al_menos_una_vez_dre += 1



            contador_caracter = 0
            tiene_dre = False


        else:
            contador_caracter += 1
            if letra == 'd':
                tiene_d = True
                tiene_dr = False
            else:
                if letra == 'r' and tiene_d:
                    tiene_dr = True
                else:
                    if letra == 'e' and tiene_dr:
                        tiene_dre = True
                    tiene_dr = False
                tiene_d = False





        anterior = letra


    porcentaje_palabras_3_letras_sobre_letras_totales = round((cant_palabras_3_letras * 100) / cant_palabras_totales, 2)


    print(f'La cantidad de palabras que tenían exáctamente 3 letras son: {cant_palabras_3_letras}')
    print(f'El porcentaje de palabras que contienen sólo 3 letras, sobre el total de las palabras del texto es de: {porcentaje_palabras_3_letras_sobre_letras_totales}%')
    print(f'La cantidad de palabras que terminan con la letra "s" es de: {cant_palabras_terminan_s}')
    print(f'La cantidad de palabras que tienen al menos una vez "dre" son: {cant_palabras_que_tienen_al_menos_una_vez_dre}')





analizarTexto()
