import random

intentos = int(input('Ingrese la cantidad de intentos para adivinar: '))
limite_derecho = int(input('Ingrese el límite derecho del intervalo: '))



for i in range(1,intentos + 1):
    num_aleatorio = random.randint(1, limite_derecho)
    opcion_jugador = int(input(f'Ingrese el número, entre 1 y {limite_derecho} que piensa que es el número secreto: '))

    if opcion_jugador != num_aleatorio:
        intentos -= 1
        print(f'Usted no acertó, le quedan {intentos}')

    else:
        print(f'Excelente, usted adivinó, el número era: {num_aleatorio}')

