def generar_matriz(filas, columnas):
    matriz = [[0] * columnas for i in range(filas)]
    print(matriz)


def popular_matriz(matriz):






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


if __name__ == '__main__':
    principal()


