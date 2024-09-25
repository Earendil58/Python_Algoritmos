def generar_matriz(filas, columnas):
    matriz = [[0] * columnas for i in range(filas)]
    return matriz


def popular_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input(f'Ingrese la cant del articulo vendido por empleado: '))
    return matriz


def mostrar_matriz_bidimensional(matriz_populada):
    for fila in matriz_populada:
        print(fila)



def principal():
    cant_art = int(input('Ingrese la cant de articulos de la tienda: '))
    while cant_art < 0 or cant_art > 99:
        print('Sólo es posible ingresar valores entre 0 y 99. Inténtelo nuevamente!')
        cant_art = int(input('Ingrese la cant de articulos de la tienda: '))

    cant_empleados = int(input('Ingrese la cant de empleados de la tienda: '))
    while cant_empleados < 0 or cant_art > 99:
        print('Sólo es posible ingresar valores entre 0 y 99. Inténtelo nuevamente!')
        cant_empleados = int(input('Ingrese la cant de empleados de la tienda: '))

    matriz_generada = generar_matriz(cant_empleados, cant_art)
    matriz_populada = popular_matriz(matriz_generada)
    mostrar_matriz_bidimensional(matriz_populada)


if __name__ == '__main__':
    principal()


