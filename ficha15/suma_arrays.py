def generador_array(tamañoArray):
    array = []
    for elemento in range(tamañoArray):
        numero = int(input('Ingrese el valor del elemento del array: '))
        array.append(numero)

    return array

def sumaArrays(array1, array2):
    longitud_arrays = len(array1)
    array_suma = [0] * longitud_arrays

    for elemento in range(longitud_arrays):
        array_suma[elemento] = array1[elemento] + array2[elemento]

    print(array_suma)

def test():
    tamaño_1 = int(input('Ingrese el tamaño deseado para el array: '))
    array_1 = generador_array(tamaño_1)
    tamaño_2 = int(input('Ingrese el tamaño deseado para el array: '))
    array_2 = generador_array(tamaño_2)
    array_suma = sumaArrays(array_1, array_2)


if __name__ == '__main__':
    test()

