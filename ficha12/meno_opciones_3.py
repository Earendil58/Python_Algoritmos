def es_positivo(numero):
    return int(numero) > 0

def impares(numero):
    return int(numero) % 2 != 0

def multiplos_tres(numero):
    return int(numero) % 3 == 0

def opcion_uno(numero):
    numeros_impares = []

    if es_positivo(numero):
        for i in range(1,numero + 1):
            if multiplos_tres(i) and impares(i):
                numeros_impares.append(i)

    else:
        print('El número no es positivo.')

    return numeros_impares


def en_orden(a,b):
    if a < b:
        return a,b
    else:
        return b,a


def es_primo(menor, mayor):
    numeros_primos = []
    menor, mayor = en_orden(menor, mayor)

    for numero in range(menor, mayor + 1):
        if numero > 1:  # Los números menores o iguales a 1 no son primos.
            es_primo = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                numeros_primos.append(numero)
    return numeros_primos




def principal():
    print('Ingrese alguna de las siguientes opciones: ')

    print('''1) Cargar un valor entero n por teclado, validando que sea mayor que 0, y mostrar todos los
            números impares y múltiplos de 3 que haya en el intervalo [1, n] (ambos incluidos)''')

    print('''2) Cargar dos valores enteros a y b por teclado, validando que 1 < a < b, y determinar si existe
            algún número primo en el intervalo [a, b]. Si existe alguno, muestre el primero que encuentre.
            Si no, informe con un mensaje.''')

    opcion = int(input('Ingrese su opción: '))

    if opcion == 1:
        numero_elegido = int(input('Ingrese el número elegido: '))
        resultado_opcion_uno = opcion_uno(numero_elegido)
        print(resultado_opcion_uno)

    elif opcion == 2:
        a = int(input('Ingrese el primer número (menor): '))
        b = int(input('Ingrese el segundo número (mayor): '))

        if 1 < a < b:
            numeros_primos = es_primo(a, b)
            if numeros_primos:
                print(f"Números primos en el intervalo [{a}, {b}]: {numeros_primos}")
            else:
                print(f"No hay números primos en el intervalo [{a}, {b}].")
        else:
            print("Por favor, ingrese valores donde 1 < a < b.")




if __name__ == '__main__':
    principal()








