

def ingresar_vector():
    vector = []
    cant_elementos = int(input('Ingrese la cant de elementos del vector: '))
    for i in range(cant_elementos):
        elemento = int(input(f'Ingrese el elemento[{i + 1}] del vector: '))
        vector.append(elemento)

    return vector




