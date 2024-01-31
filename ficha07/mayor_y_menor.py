import random

primer_par = True
primer_impar = True
numeros_aleatorios_generados = []

for i in range(8):
    numero_aleatorio = random.randint(1,100)
    numeros_aleatorios_generados.append(numero_aleatorio)

    #en la primera vuelta asigno el mayor al primero que salga

    if numero_aleatorio % 2 == 0:
        if primer_par:
            mayor_par = numero_aleatorio
        else:
            if numero_aleatorio > mayor_par:
                mayor_par = numero_aleatorio
        primer_par = False

    else:
        if primer_impar:
            menor_impar = numero_aleatorio
        else:
            if numero_aleatorio < menor_impar:
                menor_impar = numero_aleatorio
        primer_impar = False



print(f'Los números aleatorios generados fueron: {numeros_aleatorios_generados}')
print(f'El mayor número aleatorio par fue: {mayor_par}')
print(f'El menor número aleatorio impar fue: {menor_impar}')


