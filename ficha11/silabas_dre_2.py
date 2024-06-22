# Desarrollar un programa en Python que permita cargar por teclado un texto completo.
# Siempre se supone que el usuario cargará un punto para indicar el final del texto,
# y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
# El programa debe:
#
# Determinar cuántas palabras tenían exactamente 3 letras.
# Determinar el porcentaje que las palabras del punto 1 representan en el total del palabras del texto.
# Determinar cuántas palabras terminaban con la letra "s".
# Determinar cuántas palabras contuvieron al menos una vez la expresión "dre".


texto = input('Ingrese el texto: ')
texto_normalizado = texto.lower()

cant_letras_por_palabra = 0
cant_palabras_tienen_exactamente_3_letras = 0
cant_palabras_totales_en_texto = 0
cant_palabras_terminan_en_s = 0
tiene_d = False
tiene_dr = False
tiene_dre = False
cant_palabras_tienen_al_menos_una_vez_dre = 0

for letra in texto_normalizado:

    if letra == ' ' or letra == '.':

        cant_palabras_totales_en_texto += 1

        if anterior == 's':
            cant_palabras_terminan_en_s += 1

        if cant_letras_por_palabra == 3:
            cant_palabras_tienen_exactamente_3_letras += 1

        if tiene_dre:
            cant_palabras_tienen_al_menos_una_vez_dre += 1

        cant_letras_por_palabra = 0
        tiene_d = tiene_dr = tiene_dre = False

    else:
        cant_letras_por_palabra += 1

        if letra == 'd':
            tiene_d = True
        elif tiene_d and letra == 'r':
            tiene_dr = True
        elif tiene_dr and letra == 'e':
            tiene_dre = True

        anterior = letra


porcentaje_palabras_exactamente_3_letras_sobre_total_palabras_en_texto = round((cant_palabras_tienen_exactamente_3_letras * 100) / cant_palabras_totales_en_texto, 2)


print(f'La cantidad de palabras que tienen exactamente 3 letras es: {cant_palabras_tienen_exactamente_3_letras}')
print(f'El promedio de las palabras que tienen exactamente 3 letras sobre el total de las palabras del texto es de: {porcentaje_palabras_exactamente_3_letras_sobre_total_palabras_en_texto}%')
print(f'La cant de palabras que terminan con la letra "s" son: {cant_palabras_terminan_en_s}')
print(f'La cant de palabras que tienen al menos una vez "dre" son: {cant_palabras_tienen_al_menos_una_vez_dre}')
