def procesar_texto():
    tratar_archivo = open('./tps/envios25.txt', 'rt')
    texto = tratar_archivo.read()
    tratar_archivo.close()
    return texto


def procesar_oracion(texto):
    oracion = ''
    indice = 0
    longitud_texto = len(texto)

    while indice < longitud_texto:
        caracter = texto[indice]

        if caracter == '\n':
            # Si encontramos un salto de línea, procesamos la oración
            if oracion:  # Asegurarse de que no sea una línea vacía
                print(oracion.strip())
                oracion = ''
        else:
            # Agregamos el carácter a la oración actual
            oracion += caracter

        indice += 1

    # Procesar la última oración si no está vacía
    if oracion:
        print(oracion)



def main():
    texto_procesado = procesar_texto()
    procesar_oracion(texto_procesado)


main()
