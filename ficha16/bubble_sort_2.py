def buble_sort(numeros):
    longitud_array = len(numeros)

    for i in range(longitud_array):
        print(f'----Pasada: {i + 1}----')
        for j in range(0, longitud_array - i - 1):
            print(f'Esto es [j]:{numeros[j]}')
            print(f'Esto es [j + 1]: {numeros[j + 1]}')
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
                print(f'Esto es [j] dsp del cambio:{numeros[j]}')
                print(f'Esto es [j + 1] dsp del cambio: {numeros[j + 1]}')

    return numeros

array = [7,5,1,3,11,14,2,101]

array_ordenado = buble_sort(array)
