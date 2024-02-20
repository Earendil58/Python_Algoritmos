# Cargar por teclado un arreglo de n componentes y multiplicarlo por el valor k
# que también se ingresa por teclado.

def generarArreglo(longitudArreglo, factorMultiplicacion):
    arreglo = []
    for i in range(1, longitudArreglo + 1):
        arreglo.append(i * factorMultiplicacion)

    return arreglo


arreglo_1 = generarArreglo(10, 2)

print(arreglo_1)
    
