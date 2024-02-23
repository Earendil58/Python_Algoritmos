def arregloMulti(arregloUsuario, multiplicador):
    arreglo = []
    for i in arregloUsuario:
        arreglo.append(i * multiplicador)

    return arreglo


arreglo_1 = [1,2,3,4,5,6,7,8,9,10]

print(arregloMulti(arreglo_1, 2))

print(arregloMulti(arreglo_1, 3))

print(arregloMulti(arreglo_1, 200))

