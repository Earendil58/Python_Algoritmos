texto = input('Ingrese un texto: ')

texto_normalizado = texto.lower()

cant_letras = 0
cant_letras_totales = 0
cant_palabras = 0
palabra_mas_4_letras = 0
aparecio_x_o_y = False
palabras_al_menos_una_vez_x_o_y = 0

for letra in texto_normalizado:

    if letra == ' ' or letra == '.':
        if cant_letras > 0:
            cant_palabras += 1

        if cant_letras > 4:
            palabra_mas_4_letras += 1

        cant_letras = 0
        aparecio_x_o_y = False


    else:
        cant_letras += 1
        cant_letras_totales += 1

        if (letra == 'x' or letra == 'y') and not(aparecio_x_o_y):
            aparecio_x_o_y = True
            palabras_al_menos_una_vez_x_o_y += 1


promedio_letras_texto =round(cant_letras_totales / cant_palabras, 2)


print(f'La cantidad de palabras con más de 4 letras son: {palabra_mas_4_letras}')
print(f'La cant de palabras en las que aparecen al menos una vez "x" o "y" son: {palabras_al_menos_una_vez_x_o_y}')
print(f'La cant de letras por palabra, en promedio, en el texto es de: {promedio_letras_texto}')



