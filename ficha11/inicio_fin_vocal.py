def contar_palabras_vocales(texto):
    palabras = texto.split()  # Divide el texto en palabras separadas por espacios
    total_palabras = len(palabras)
    contador_vocales = 0
    contador_misma_letra = 0
    letra_anterior = None

    for palabra in palabras:
        if palabra[0].lower() in "aeiouáéíóúü" and palabra[-1].lower() in "aeiouáéíóúü":
            contador_vocales += 1

        if letra_anterior is not None and palabra[0].lower() == letra_anterior.lower():
            contador_misma_letra += 1

        letra_anterior = palabra[-1]

    porcentaje_vocales = (contador_vocales / total_palabras) * 100

    return contador_vocales, contador_misma_letra, porcentaje_vocales


texto_ingresado = input("Ingresa un texto (finaliza con un punto): ")

if texto_ingresado[-1] != ".":
    texto_ingresado += "."

resultado_a, resultado_b, resultado_c = contar_palabras_vocales(texto_ingresado)

print("a) Cantidad de palabras que comienzan y terminan en vocal:", resultado_a)
print("b) Cantidad de palabras que comienzan con la misma letra que terminó la palabra anterior:", resultado_b)
print("c) Porcentaje que representa el punto a) sobre el total de palabras del texto:", resultado_c)

