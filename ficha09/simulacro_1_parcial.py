import random

random.seed(49)

rango = 20000
sumatorio_todos_num = 0

#PUNTO 1
numeros_multiplos_5 = 0
numeros_multiplos_7 = 0
numeros_multiplos_9 = 0

#PUNTO 2
numero_mayor_ultimo_digito_mayor_igual_6_pero_menor_igual_8 = 0

#PUNTO 3
numeros_pares_menores_15000 = 0

#PUNTO 4
porcentaje_numeros_pares_menores_15000 = 0


for i in range(rango):

    num_aleatorio = random.randint(1, 45000)

    sumatorio_todos_num += num_aleatorio


    #LOGICA PUNTO 1
    if num_aleatorio % 5 == 0:
        numeros_multiplos_5 += 1

    if num_aleatorio % 7 == 0:
        numeros_multiplos_7 += 1

    if num_aleatorio % 9 == 0:
        numeros_multiplos_9 += 1


    #LOGICA PUNTO 2
    if ((num_aleatorio % 10) >= 5) and ((num_aleatorio % 10) <= 8):
        if num_aleatorio > numero_mayor_ultimo_digito_mayor_igual_6_pero_menor_igual_8:
            numero_mayor_ultimo_digito_mayor_igual_6_pero_menor_igual_8 = num_aleatorio


    #LOGICA PUNTO 3
    if ((num_aleatorio % 2) == 0) and num_aleatorio < 15_000:
        numeros_pares_menores_15000 += 1

    #LOGICA PUNTO 4
    porcentaje_numeros_pares_menores_15000 = (numeros_pares_menores_15000 * 100) // 20000


print(f'La sumatoria de todos los números es: {sumatorio_todos_num}')

#PRINT PUNTO 1
print(f'La cantidad de números múltiplos de 5 son: {numeros_multiplos_5}')
print(f'La cantidad de números múltiplos de 7 son: {numeros_multiplos_7}')
print(f'La cantidad de números múltiplos de 9 son: {numeros_multiplos_9}')

#PRINT PUNTO 2
print(f'El mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8 :{numero_mayor_ultimo_digito_mayor_igual_6_pero_menor_igual_8}')

#PRINT PUNTO 3
print(f'La cantidad de números pares y menores a 15000 son: {numeros_pares_menores_15000}')

#PRINT PUNTO 4
print(f'El porcentaje de números generados son pares menores a 15000 sobre el total es de: {porcentaje_numeros_pares_menores_15000}%')
