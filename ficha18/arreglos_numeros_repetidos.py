
def popular_array(cant_elementos):
    array = []
    for elemento in range(cant_elementos):
        elemento_a_añadir = int(input(f'Ingrese el elemento {elemento + 1}: '))
        array.append(elemento_a_añadir)

    return array

def chequear_repeticion(arr1, arr2):
    num_repetido = []
    for i in arr1:
        for j in arr2:
            if i == j:
                num_repetido.append(i)

    return num_repetido



def principal():
    cant_elementos_primer_array = int(input('Ingrese la cant de elem del primer array: '))
    cant_elementos_segundo_array = int(input('Ingrese la cant de elem del segundo array: '))

    array_1 = popular_array(cant_elementos_primer_array)
    array_2 = popular_array(cant_elementos_segundo_array)

    print(f'El primer array contiene los elementos: {array_1}')
    print(f'El segundo array contiene los elementos: {array_2}')

    num_repetidos = chequear_repeticion(array_1, array_2)

    print(f'Los números repetidos, en los arrays ingresados son: {num_repetidos}')




if __name__ == '__main__':
    principal()
