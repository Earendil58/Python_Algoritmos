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

        if contador_letra > 1:
            contador_palabras += 1
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
            if letra in vocales:
                comienza_vocal = True

            if letra == ultima_letra_palabra:
                cant_palabras_comienzan_como_termino_palabra_anterior += 1

        anterior = letra


promedio_palabras_empiezan_terminan_vocal_sobre_total_texto = (cant_palabras_comienzan_terminan_en_vocal * 100) // contador_palabras


print(f'La cant de palabras en el texto que comienzan y terminan con vocales son: {cant_palabras_comienzan_terminan_en_vocal}')
print(f'La cant de palabras en el texto que comienzan con la misma letra que termina la palabra anterior es de: {cant_palabras_comienzan_como_termino_palabra_anterior}')
print(f'La cantidad de palabras totales en el texto son: {contador_palabras}')
print(f'El promedio de las palabras que empiezan y terminan en vocal sobre la cant de palabras totales del texto es: {promedio_palabras_empiezan_terminan_vocal_sobre_total_texto}%')

