texto = input('Ingrese un texto: ')

texto_normalizado = texto.lower()

contador_palabras = 0
contador_letra = 0
anterior = ''
vocales = 'aeiou'
comienza_vocal = 0
termina_vocal = 0
cant_palabras_comienzan_terminan_en_vocal = 0
primera_letra = True
primera_letra_palabra = ''
ultima_letra_palabra = ''
cant_palabras_comienzan_como_termino_palabra_anterior = 0


for letra in texto_normalizado:

    contador_letra += 1

    if letra == ' ' or letra == '.':

        print(f'ULTIMA LETRA: {anterior}')

        if contador_letra > 1:
            ultima_letra_palabra = anterior

        if ultima_letra_palabra in vocales:
            termina_vocal = True

        if comienza_vocal and termina_vocal:
            cant_palabras_comienzan_terminan_en_vocal += 1

        comienza_vocal = False
        termina_vocal = False
        contador_letra = 0

    else:
        if contador_letra == 1:
            print(f'Primera letra: {letra}')
            if letra in vocales:
                comienza_vocal = True


            if letra == ultima_letra_palabra:
                cant_palabras_comienzan_como_termino_palabra_anterior += 1


        anterior = letra


print(f'La cant de palabras en el texto que comienzan y terminan con vocales son: {cant_palabras_comienzan_terminan_en_vocal}')
print(f'La cant de palabras en el texto que comienzan con la misma letra que termina la palabr anterior es de: {cant_palabras_comienzan_como_termino_palabra_anterior}')


