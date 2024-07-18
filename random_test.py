def generador_arrays(cantArrays):
    conjunto_arrays = []

    if cantArrays > 0:
        for _ in range(cantArrays):
            array = []
            conjunto_arrays.append(array)
        return conjunto_arrays

def popular_arrays(conjuntoArrays):
    for i in range(len(conjuntoArrays)):
        if len(conjuntoArrays[i]) == 0:
            tamaño_array = int(input('Ingrese el tamaño del array: '))
            array = [0] * tamaño_array
            conjuntoArrays[i] = array
    print(f'Los arrays populados: {conjuntoArrays}')
    return conjuntoArrays

def test():
    cant_arrays = int(input('Ingrese la cantidad de arrays a generar: '))
    arrays_a_popular = generador_arrays(cant_arrays)
    popular_arrays(arrays_a_popular)

if __name__ == '__main__':
    test()
