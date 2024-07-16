def arreglo(lista, multiplicador):
    lista_multiplicada = []

    for elemento in lista:
        elemento_multiplicado = elemento * multiplicador

        lista_multiplicada.append(elemento_multiplicado)

    return lista_multiplicada


def test():
    array = []
    largo_lista = int(input('Ingrese el largo tamaño del array: '))
    multiplicador = int(input('Ingrese el elemento multiplicador: '))

    for i in range(largo_lista):
        elemento_array = int(input('Ingrese un elemento del array: '))
        array.append(elemento_array)


    arreglo_multiplicado = arreglo(array, multiplicador)

    print(arreglo_multiplicado)


if __name__ == '__main__':
    test()


