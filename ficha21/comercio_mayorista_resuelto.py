def validate(inf):
    t = inf
    while t <= inf:
        t = int(input('Ingrese valor (mayor a ' + str(inf) + ' por favor): '))
        if t <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return t


def read(m, n):
    # crear y cargar por teclado una matriz... por filas en orden creciente...
    # m filas - n columnas...
    cant = [[0] * n for f in range(m)]
    for f in range(m):
        for c in range(n):
            cant[f][c] = int(input('Valor [' + str(f) + '][' + str(c) + ']: '))
    return cant


def totales_por_vendedor(cant):
    # totalización por filas...
    m, n = len(cant), len(cant[0])
    print()
    print('Cantidades vendidas por cada vendedor')
    for f in range(m):
        ac = 0
        for c in range(n):
            ac += cant[f][c]
        print('Vendedor', f, '\t- Cantidad total vendida:', ac)


def totales_por_articulo(cant):
    # totalización por columnas...
    m, n = len(cant), len(cant[0])
    print()
    print('Cantidades totales vendidas de cada artículo')
    for c in range(n):
        ac = 0
        for f in range(m):
            ac += cant[f][c]
        print('Artículo', c, '\t- Cantidad total vendida:', ac)


def test():
    print('Cantidad de vendedores...')
    m = validate(0)

    print('Cantidad de artículos...')
    n = validate(0)

    print('Cargue las cantidades de artículos por vendedor...')
    cant = read(m, n)

    totales_por_vendedor(cant)
    totales_por_articulo(cant)


if __name__ == '__main__':
    test()
