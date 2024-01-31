

def contadorSilabasMo(texto):
    cant_palabras_mas_4_letras = 0
    tiene_x_y = False
    cant_palabras_con_x_y = 0
    cant_letra_por_palabra = 0
    cant_letras_totales = 0
    cant_palabras = 0
    anterior = ''
    tuvo_mo = 0
    expresion_mo_por_palabra = 0

    for letra in texto:
        letra = letra.lower()

        if letra == ' ' or letra == '.':
            cant_palabras += 1

            if cant_letra_por_palabra > 4:
                cant_palabras_mas_4_letras += 1

            if tiene_x_y:
                cant_palabras_con_x_y += 1

            if tuvo_mo == 1:
                expresion_mo_por_palabra += 1

            tiene_x_y = False
            tuvo_mo = 0
            cant_letra_por_palabra = 0

        else:
            cant_letra_por_palabra += 1
            cant_letras_totales += 1

            if letra == 'x' or letra == 'y':
                tiene_x_y = True

            if letra == 'm' and anterior == 'o':
                tuvo_mo += 1


        anterior = letra


    if cant_palabras == 0:
        promedio = 0

    else:
        promedio = round((cant_letras_totales / cant_palabras), 2)


    # print(f'El promedio de letras por palabra en el texto es de: {promedio}%')
    # print(f'La cantidad de palabras que contienen x o y en el texto es de: {cant_palabras_con_x_y}')
    # print(f'La cantidad de palabras en el texto es de: {cant_palabras}')
    # print(f'La cantidad de palabras que tienen más de 4 letras en el texto es de: {cant_palabras_mas_4_letras}')
    # print(f'La cantidad de palabras que poseen solamente una vez la expresión "mo" son: {expresion_mo_por_palabra}')

    return promedio, cant_palabras_mas_4_letras, cant_palabras_con_x_y, expresion_mo_por_palabra


texto_a_analizar = 'Hola, soy un texto a analizar, debo ver si el mismo tenía la expresion mo como momentaneamente estoy asumiento que lo tiene monisilabos no quiero poner, pero a veces se necesitan'

resultados_tupla_texto_a_analizar = contadorSilabasMo(texto_a_analizar)

resultado_promedio, resultado_mas_4_letras, resultado_con_x_y, resultado_mo_por_palabra = resultados_tupla_texto_a_analizar

print("Promedio de letras por palabra:", resultado_promedio)
print("Palabras con más de 4 letras:", resultado_mas_4_letras)
print("Palabras con 'x' o 'y':", resultado_con_x_y)
print("Expresiones 'mo' por palabra:", resultado_mo_por_palabra)



