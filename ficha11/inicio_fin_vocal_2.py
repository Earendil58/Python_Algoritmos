texto = input('Ingrese un texto: ')

texto_normalizado = texto.lower()

contador_palabras = 0
contador_letra = 0
anterior = ''
vocales = 'aeiou'
comienzan_vocal = 0
primera_letra = True
primera_letra_palabra = ''
ultima_letra_palabra = ''
cant_palabras_comienzan_como_termino_palabra_anterior = 0


for letra in texto_normalizado:

    if letra == ' ' or letra == '.':

        ultima_letra_palabra = anterior

        contador_letra = 0

    else:
        contador_letra += 1

        if contador_letra == 1:
            if letra in vocales:
                comienzan_vocal += 1
            if letra == ultima_letra_palabra:
                cant_palabras_comienzan_como_termino_palabra_anterior += 1
                print(f'Esta es la última letra: {ultima_letra_palabra}')

        anterior = letra


print(f'La cant de palabras en el texto que comienzan con vocales son: {comienzan_vocal}')
print(f'La cant de palabras en el texto que comienzan con la misma letra que termina la palabr anterior es de: {cant_palabras_comienzan_como_termino_palabra_anterior}')


