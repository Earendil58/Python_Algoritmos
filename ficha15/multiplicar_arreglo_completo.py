
def validador():
    logitud_arreglo = 0
    while logitud_arreglo <= 0:
        logitud_arreglo = int(input('Ingrese la cantidad de elementos que quiere para el arreglo(cant. positiva): '))

    arreglo = []
    for i in range(logitud_arreglo):
        variable_auxiliar = int(input(f'Ingrese un número para el arreglo, ingresando indice[{i + 1}]: '))
        arreglo.append(variable_auxiliar)


    return arreglo



def multiplicadorArreglo():
    factor = int(input('Ingrese el factor por el cual desea multiplicar el arreglo: '))
    arreglo = validador()
    arreglo_multiplicado = []

    for i in arreglo:
        arreglo_multiplicado.append(i * factor)

    print(arreglo_multiplicado)


multiplicadorArreglo()
