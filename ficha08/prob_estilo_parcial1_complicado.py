import random

random.seed(37)


#PUNTO 1
contador = 0
mayores_menos_20000_menores_menos_5000 = 0
mayores_o_iguales_menos_5000_pero_menores_15000 = 0
mayores_o_iguales_15000_pero_divisible_por_9 = 0

#PUNTO 2
todos_num_mayores_o_iguales_1000_pero_ultimo_dig_igual_4_6 = 0
conteo_promedio_entero_de_num_mayores_o_iguales_1000_pero_ultimo_dig_igual_4_6 = 0

#PUNTO 3
mayor_todos_num_positivos_impar_ademas_ult_dig_diferente_1 = 0

#PUNTO 4
cantidad_num_divisibles_por_7 = 0

while contador < 27_000:
    contador += 1

    #PUNTO 1
    num_aleatorio = random.randint(-20_000,30_000)

    if (num_aleatorio >= -20_000) and (num_aleatorio < -5000):
        mayores_menos_20000_menores_menos_5000 += 1

    elif (num_aleatorio >= -5000) and (num_aleatorio < 15000):
        mayores_o_iguales_menos_5000_pero_menores_15000 += 1

    elif (num_aleatorio >= 15000) and ((num_aleatorio % 9) == 0):
        mayores_o_iguales_15000_pero_divisible_por_9 += 1


    #PUNTO 2

    if (num_aleatorio >= 1000) and ((num_aleatorio % 10 == 4) or (num_aleatorio % 10 == 6)):
        todos_num_mayores_o_iguales_1000_pero_ultimo_dig_igual_4_6 += num_aleatorio
        conteo_promedio_entero_de_num_mayores_o_iguales_1000_pero_ultimo_dig_igual_4_6 += 1

    #PUNTO 3
    if ((num_aleatorio % 2) != 0) and ((num_aleatorio % 10) != 1):
        if num_aleatorio > mayor_todos_num_positivos_impar_ademas_ult_dig_diferente_1:
            mayor_todos_num_positivos_impar_ademas_ult_dig_diferente_1 = num_aleatorio

    #PUNTO 4
    if num_aleatorio % 7 == 0:
        cantidad_num_divisibles_por_7 += 1





promedio_todos_num_mayores_o_iguales_1000_pero_ultimo_dig_igual_4_6 = (todos_num_mayores_o_iguales_1000_pero_ultimo_dig_igual_4_6) // conteo_promedio_entero_de_num_mayores_o_iguales_1000_pero_ultimo_dig_igual_4_6
porcentaje_de_numeros_div_por_7_sobre_total = (cantidad_num_divisibles_por_7 * 100) // 27000




#PRINT DE PUNTO 1:
print(f'La cantidad de números son mayores o iguales que -20000 pero menores que -5000, son: {mayores_menos_20000_menores_menos_5000}')
print(f'La cantidad de números que son mayores o iguales a -5000 pero menores que 15000, son: {mayores_o_iguales_menos_5000_pero_menores_15000}')
print(f'La cantidad de números que son mayores o iguales que 15000 pero además son divisibles por 9, son: {mayores_o_iguales_15000_pero_divisible_por_9}')


#PRINT DE PUNTO 2:
print(f'El promedio entero de todos los números generados que sean mayores o iguales a 1000 peroque además tengan su último dígito igual a 4 o a 6 es de: {promedio_todos_num_mayores_o_iguales_1000_pero_ultimo_dig_igual_4_6}')


#PRINT DE PUNTO 3:
print(f'El mayor entre todos los números generados que sean positivos impares, pero que además tengan su último digito diferente de 1 es: {mayor_todos_num_positivos_impar_ademas_ult_dig_diferente_1}')

#PRINT DE PUNTO 4:
print(f'El porcentaje de números divisibles por 7, sobre el total de números iterados es: {porcentaje_de_numeros_div_por_7_sobre_total}%')


