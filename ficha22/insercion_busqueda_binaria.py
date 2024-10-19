def busqueda_binaria(arreglo, valor):
    izq, der = 0, len(arreglo) - 1

    print(f'Limite izq: {izq}')
    print(f'Limite der: {der}')

    while izq <= der:
        punto_medio = (izq + der) // 2

        print(f'Punto medio: {punto_medio}')

        if arreglo[punto_medio] < valor:
            izq = punto_medio + 1

        else:
            der = punto_medio - 1


    return izq



def add_in_order(arreglo, valor):
    pos = busqueda_binaria(arreglo,valor)
    arreglo.insert(pos,valor)


arreglo = [1, 3, 5, 7, 9, 11, 13, 15]

add_in_order(arreglo, 10)

print(arreglo)
