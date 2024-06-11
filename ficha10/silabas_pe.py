texto = input('Ingrese su texto: ')

texto_normalizado = texto.lower()

#VARIABLES AUXILIARES
cant_letras_por_palabra = 0
cant_letras_totales_en_texto = 0

palabras_3_letras = 0
palabras_5_letras = 0
palabras_7_letras = 0

vocales = 'aeiou'
tercera_letra = ''
palabras_vocal_tercera = 0

for letra in texto_normalizado:

    if letra == ' ' or letra == '.':

        if cant_letras_por_palabra == 3:
            palabras_3_letras += 1

        elif cant_letras_por_palabra == 5:
            palabras_5_letras += 1

        elif cant_letras_por_palabra == 7:
            palabras_7_letras += 1

        if cant_letras_por_palabra > 3 and tercera_letra in vocales:
            palabras_vocal_tercera += 1

        cant_letras_por_palabra = 0

    else:
        cant_letras_por_palabra += 1
        cant_letras_totales_en_texto += 1

        if cant_letras_por_palabra == 3:
            tercera_letra = letra



print(f'La cant de palabras que tienen 3 letras son: {palabras_3_letras}')
print(f'La cant de palabras que tienen 5 letras son: {palabras_5_letras}')
print(f'La cant de palabras que tienen 7 letras son: {palabras_7_letras}')
print(f'La cant de palabras que tienen más de 3 letras y la tercera letra es una vocal son: {palabras_vocal_tercera}')




