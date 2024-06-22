# El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero.
# La frase finaliza con un punto, y las palabras están separadas por espacios únicamente.
# Se debe mostrar:
#
# Ver el porcentaje de vocales respecto del total de letras de la frase.
# La longitud promedio de las palabras
# La longitud de la palabra mas larga del texto
# Cantidad de palabras que comienzan con "ta"


texto = input('Ingrese el texto: ')
texto_normalizado = texto.lower()

vocales = 'aeiou'
cant_vocales = 0
cant_palabras_en_texto = 0
cant_letras_por_palabra = 0
cant_letras_totales_en_texto = 0
sumatorio_cant_letras_por_palabra = 0
longitud_palabra_mas_larga = 0
cant_palabras_comienzan_con_ta = 0
anterior = ''
aparecio_ta = False
cant_veces_aparecio_ta = 0

for letra in texto_normalizado:

    if letra == ' ' or letra == '.':

        if longitud_palabra_mas_larga == 0:
            longitud_palabra_mas_larga = cant_letras_por_palabra

        elif cant_letras_por_palabra > longitud_palabra_mas_larga:
            longitud_palabra_mas_larga = cant_letras_por_palabra

        cant_palabras_en_texto += 1
        sumatorio_cant_letras_por_palabra += cant_letras_por_palabra
        cant_letras_por_palabra = 0


    else:
        cant_letras_por_palabra += 1
        cant_letras_totales_en_texto += 1

        if letra in vocales:
            cant_vocales += 1

        if letra == 'a' and anterior == 't':
            aparecio_ta = True
            cant_veces_aparecio_ta += 1

        anterior = letra


longitud_promedio_de_palabras_en_texto = sumatorio_cant_letras_por_palabra // cant_palabras_en_texto
porcentaje_vocales_sobre_letras_totales_en_texto = round((cant_vocales * 100) / cant_letras_totales_en_texto, 2)


print(f'La longitud, promedio, de palabras en el texto es de: {longitud_promedio_de_palabras_en_texto}')
print(f'La longitud de la palabra más larga del texto es de: {longitud_palabra_mas_larga}')
if aparecio_ta:
    print(f'Aparecio "ta", fueron :{cant_veces_aparecio_ta} veces.')

print(f'El porcentaje de vocales, sobre el total de letras en el texto, es de: {porcentaje_vocales_sobre_letras_totales_en_texto}%')



