#FUNCIONES LOGICAS

def validadorPositivos(inf):
    numero = inf - 1
    while numero < inf:
        numero = int(input('Por favor ingrese un número positivo: '))

    return numero


def imparesMultiplosTres(limiteDerecho):
    impares_multiplos_tres = []

    for numero in range(3, limiteDerecho + 1, 6):
        impares_multiplos_tres.append(numero)

    return impares_multiplos_tres

def chequearOrden():
    numeros = []
    numero = int(input('Ingrese un número: '))
    anterior = numero
    creciente = True
    while numero != 0:
        numeros.append(numero)
        numero = int(input('Ingrese otro número: '))

        if numero < anterior and numero != 0:
            creciente = False

    return creciente, numeros

def es_primo(numero):
    if numero < 0:
        return None
    elif numero == 1 :
        return False
    elif numero == 2:
        return True
    if numero % 2 == 0:
        return False

    raiz = int(pow(numero, 0.5))
    for divisor in range(3, raiz + 1, 2):
        if numero % divisor == 0:
            return False
    return True

def proximo_primo(numero):
    if numero < 2:
        return 2

    p = numero + 1
    if p % 2 == 0:
        p +=1

    while not es_primo(p):
        p += 2

    return p

def buscar_primo(a,b):
    p = proximo_primo(a - 1)

    if p <= b:
        return p

    return None


#FUNCIONES GENERALES CON INTERACCION GRAFICA

def opcionUno():
    numero_positivo = validadorPositivos()
    impares_multiplos_tres = imparesMultiplosTres(numero_positivo)
    print(impares_multiplos_tres)


def opcionDos():
    a = validadorPositivos(1)
    b = validadorPositivos(a)
    primo = buscar_primo(a,b)
    if primo is not None:
        print(f'Hay al menos un numero primo en el intervalo: [{a}, {b}]')
    else:
        print('No hay primos en el intervalo')


def opcionTres():
    creciente, numeros_ingresados = chequearOrden()
    if creciente:
        print('Los números están ordenados de menor a mayor')
    else:
        print('Los números no están ordenados de menor a mayor')

    print(f'Los números son: {numeros_ingresados}')


#FUNCION DE MENU

def menu():
    opcion = -1

    while 1 > opcion or opcion > 4:
        print('Elije alguna de las siguientes opciones: ')
        print('1) Mostrar todos los números impares y múltiplos de 3 que haya en el intervalo [1, n] (ambos incluidos)')
        print('2) Determinar si existe algún número primo en el intervalo [a, b], cargados por teclado. Si existe alguno, muestre el primero que encuentre.Si no, informe con un mensaje')
        print('3) Cargar por teclado una secuencia de números uno a uno,'
                    'cortando el proceso cuando el número cargado sea el 0. '
                    'Determinar si todos los números entraron ordenados de menor a mayor')

        opcion = int(input('Ingrese su opción: '))

    if opcion == 1:
        opcionUno()

    elif opcion == 2:
        opcionDos()

    elif opcion == 3:
        opcionTres()


menu()
