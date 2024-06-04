import random

mayor_par = None
menor_impar = None
numeros_aleatorios = []

for numero in range(1,9):
    numero_aleatorio = random.randint(1,100)
    numeros_aleatorios.append(numero_aleatorio)

    if mayor_par is None and numero_aleatorio % 2 == 0:
        mayor_par = numero_aleatorio

    else:
        if ((numero_aleatorio % 2) == 0) and (numero_aleatorio > mayor_par):
            mayor_par = numero_aleatorio


    if menor_impar is None and numero_aleatorio % 2 !=0:
        menor_impar = numero_aleatorio

    else:
        if ((numero_aleatorio % 2) != 0) and (numero_aleatorio < menor_impar):
            menor_impar = numero_aleatorio



print(f'Los números aleatorios fueron: {numeros_aleatorios}')
print(f'El mayor de los números pares es: {mayor_par}')
print(f'El menor de los números impares es: {menor_impar}')
