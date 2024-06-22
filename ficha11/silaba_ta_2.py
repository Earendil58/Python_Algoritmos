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

cant_vocales = 0
cant_palabras_en_texto = 0
cant_letras_por_palabra = 0
sumatorio_cant_letras_por_palabra = 0
longitud_palabra_mas_larga = 0
cant_palabras_comienzan_con_ta = 0

for letra in texto_normalizado:

    if letra == ' ' or letra == '.':

        cant_palabras_en_texto += 1
        sumatorio_cant_letras_por_palabra += cant_letras_por_palabra
        cant_letras_por_palabra = 0


    else:
        cant_letras_por_palabra += 1


longitud_promedio_de_palabras_en_texto = sumatorio_cant_letras_por_palabra // cant_palabras_en_texto


print(f'La longitud, promedio, de palabras en el texto es de: {longitud_promedio_de_palabras_en_texto}')



