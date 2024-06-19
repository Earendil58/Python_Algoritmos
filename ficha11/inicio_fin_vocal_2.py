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

        print(f'la cant de letras es: {contador_letra}')

        if primera_letra_palabra == ultima_letra_palabra:
            cant_palabras_comienzan_como_termino_palabra_anterior += 1

        contador_letra = 0
        primera_letra = True

    else:
        contador_letra += 1

        if primera_letra and letra in vocales and contador_letra != 1:
            comienzan_vocal += 1
            primera_letra = False
            print(f'Esta es la letra que se contó como vocal: {letra}')


print(f'La cant de palabras en el texto que comienzan con vocales son: {comienzan_vocal}')
print(f'La cant de palabras en el texto que comienzan con la misma letra que termina la palabr anterior es de: {cant_palabras_comienzan_como_termino_palabra_anterior}')


