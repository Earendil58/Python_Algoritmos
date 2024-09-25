def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [0] * columnas
        matriz.append(fila)


    return matriz


matriz_generada = generar_matriz(3,3)

for fila in matriz_generada:
    print(fila)

