import random

random.seed(37)

#PUNTO 1
mayores_o_iguales_menos_20000_menores_que_menos_5000 = 0
mayores_o_iguales_menos_5000_pero_menores_15000 = 0
mayores_o_iguales_15000_pero_divisibles_por_9 = 0
#PUNTO 2
cant_may_o_iguales_1000_ultimo_dig_4_o_6 = 0
acumulador_may_o_iguales_1000_ultimo_dig_4_o_6 = 0
#PUNTO 3
mayor_positivos_impares_ultimo_dig_diferente_1 = -20001
#PUNTO 4
cant_num_divisible_por_7 = 0

for i in range(27000):
    numero = random.randint(-20000, 30000)


#PUNTO NUMERO 1
    if -20000 <= numero < -5000:
        mayores_o_iguales_menos_20000_menores_que_menos_5000 += 1

    elif -5000 <= numero < 15000:
        mayores_o_iguales_menos_5000_pero_menores_15000 += 1

    elif 15000 <= numero and numero % 9 == 0:
        mayores_o_iguales_15000_pero_divisibles_por_9 += 1

#PUNTO NUMERO 2

    if (numero >= 1000) and (numero % 10 == 4 or numero % 10 == 6):
        cant_may_o_iguales_1000_ultimo_dig_4_o_6 += 1
        acumulador_may_o_iguales_1000_ultimo_dig_4_o_6 += numero


#PUNTO NUMERO 3

    if (numero > mayor_positivos_impares_ultimo_dig_diferente_1) and (numero > 0) and (numero % 2 != 0) and (numero % 10 != 1):
        mayor_positivos_impares_ultimo_dig_diferente_1 = numero


#PUNTO NUMERO 4
    if numero % 7 == 0:
        cant_num_divisible_por_7 += 1




promedio_may_o_iguales_1000_ultimo_dig_4_o_6 = (acumulador_may_o_iguales_1000_ultimo_dig_4_o_6) // cant_may_o_iguales_1000_ultimo_dig_4_o_6
porcentaje_cant_num_divisible_por_7 = (cant_num_divisible_por_7 * 100) // 27000

print('-'*90)
print('Respuestas punto 1): ')
print(f'La cant de num que son mayores o iguales a -20000 y menores que -5000 son: {mayores_o_iguales_menos_20000_menores_que_menos_5000}')
print(f'La cant de num que son mayores o iguales a -5000 y menores que 15000 son: {mayores_o_iguales_menos_5000_pero_menores_15000}')
print(f'La cant de num que son mayores a 15000 y divisibles por 9, es de: {mayores_o_iguales_15000_pero_divisibles_por_9}')
print('-'*90)
print('Respuestas punto 2): ')
print(f'La cant de num que son mayores o iguales a 1000, cuyo último dígito termina en 4 o 6, es de : {cant_may_o_iguales_1000_ultimo_dig_4_o_6}')
print(f'El promedio de los números que son mayores o iguales a 1000, cuyo último dígito terminaen 4 o 6 es: {promedio_may_o_iguales_1000_ultimo_dig_4_o_6}')
print('-'*90)
print('Respuestas punto 3): ')
print(f'El número mayor, positivo e impar, con último dígito diferente de 1 es: {mayor_positivos_impares_ultimo_dig_diferente_1}')
print('-'*90)
print('Respuestas punto 4): ')
print(f'El porcentaje de la cant de numeros divisibles por 7 es de: {porcentaje_cant_num_divisible_por_7}')

