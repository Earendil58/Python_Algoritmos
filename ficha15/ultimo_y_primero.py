def ultimo_elemento(vector):
    ultimo_elemento_vector = vector[-1]
    cant_veces_repetido_ultimo_elemento = 0

    for elemento in vector:
        if elemento == ultimo_elemento_vector:
            cant_veces_repetido_ultimo_elemento += 1
    return cant_veces_repetido_ultimo_elemento




def test():
    vector_tamaño = int(input('Indique de qué tamaño será el vector generado: '))
    vector = []
    for elemento in range(vector_tamaño):
        numero = int(input(f'Ingrese el elemento ({elemento + 1}) del vector: '))
        vector.append(numero)


    cant_veces_repetido_ultimo_elemento_vector = ultimo_elemento(vector)
    print(f'La cantidad de veces que estuvo repetido el último elemento del vector ({vector[-1]}) fue: {cant_veces_repetido_ultimo_elemento_vector}')

    print(vector)


if __name__ == '__main__':
    test()
