

def ingresar_vector():
    vector = []
    cant_elementos = int(input('Ingrese la cant de elementos del vector: '))
    for i in range(cant_elementos):
        elemento = int(input(f'Ingrese el elemento[{i + 1}] del vector: '))
        vector.append(elemento)

    return vector



def main():
    vector_resultante = []
    cant_vectores = int(input('Ingrese la cant de vectores: '))
    for i in range(cant_vectores):
        vector = ingresar_vector()
        vector_resultante.append(vector)

    print(vector_resultante)


if __name__ == "__main__":
    main()
