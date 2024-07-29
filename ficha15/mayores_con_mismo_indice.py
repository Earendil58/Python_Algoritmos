def comparacion_componentes_homologas(vector_uno, vector_dos):
    nuevo_vector = [0] * len(vector_uno)

    for elemento in range(len(vector_uno)):
        if vector_uno[elemento] >= vector_dos[elemento]:
            nuevo_vector[elemento] = vector_uno[elemento]
        else:
            nuevo_vector[elemento] = vector_dos[elemento]

    return nuevo_vector


def principal():
    tamaño_vectores = int(input('Ingrese el tamaño de los vectores a ingresar: '))
    primer_vector = []
    segundo_vector = []

    for elemento in range(tamaño_vectores):
        elemento_uno = int(input(f'Ingrese el elemento ({elemento + 1}) del vector 1: '))
        primer_vector.append(elemento_uno)
        elemento_dos = int(input(f'Ingrese el elemento ({elemento + 1}) del vector 2: '))
        segundo_vector.append(elemento_dos)

    print(f'El primer vector es: {primer_vector}')
    print(f'El segundo vector es: {segundo_vector}')

    nuevo_vector_elementos_homologos_mayores = comparacion_componentes_homologas(primer_vector, segundo_vector)
    print(f'El nuevo vector, con los elementos homologos mayores es: {nuevo_vector_elementos_homologos_mayores}')


if __name__ == '__main__':
    principal()




