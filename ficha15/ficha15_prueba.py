def leerArreglo(v):
    vector = [0] * v
    for i in range(v):
        vector[i] = int(input(f'Ingrese el componente [{i + 1}] del vector: '))

    print(vector)


leerArreglo(5)
