def ultimo_elemento(vector):
    ultimo_elemento_vector = vector[-1]
    cant_veces_repetido_ultimo_elemento = 0

    for elemento in vector:
        if elemento == ultimo_elemento_vector:
            cant_veces_repetido_ultimo_elemento += 1
    return cant_veces_repetido_ultimo_elemento


def primer_elemento(vector):
    primer_elemento_vector = vector[0]
    vector_con_elementos_menores_a_primer_elemento = []
    for elemento in vector:
        if elemento < primer_elemento_vector:
            vector_con_elementos_menores_a_primer_elemento.append(elemento)

    return vector_con_elementos_menores_a_primer_elemento


def test():
    vector_tamaño = int(input('Indique de qué tamaño será el vector generado: '))
    vector = []
    for elemento in range(vector_tamaño):
        numero = int(input(f'Ingrese el elemento ({elemento + 1}) del vector: '))
        vector.append(numero)


    cant_veces_repetido_ultimo_elemento_vector = ultimo_elemento(vector)
    print(f'La cantidad de veces que estuvo repetido el último elemento del vector ({vector[-1]}) fue: {cant_veces_repetido_ultimo_elemento_vector}')

    vector_con_elementos_menores_a_primer_elemento_del_vector = primer_elemento(vector)
    print(f'El array formado con elementos menores que el primer elemento del mismo es: {vector_con_elementos_menores_a_primer_elemento_del_vector}')

    print(vector)


if __name__ == '__main__':
    test()
