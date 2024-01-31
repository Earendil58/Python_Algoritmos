import random

random.seed(11)

numeros_divisibles_por_4 = 0
numeros_divisibles_por_8 = 0
numeros_divisibles_por_4_y_por_8 = 0
numeros_divisibles_por_4_pero_no_8 = 0
numeros_mayores_2000 = 0
primer_valor_generado = None
numeros_menores_primer_valor_generado = 0
aparece_1 = False
aparece_2500 = False

for i in range(1,1001):
    numero_aleatorio = random.randint(1,2500)

    if i == 1:
        primer_valor_generado = numero_aleatorio


    #PRIMER PUNTO
    if numero_aleatorio % 4 == 0 and numero_aleatorio % 8 == 0:
        numeros_divisibles_por_4_y_por_8 += 1

    elif numero_aleatorio % 4 == 0 and numero_aleatorio % 8 != 0:
       numeros_divisibles_por_4_pero_no_8 += 1


    elif numeros_divisibles_por_4 % 4 == 0:
        numeros_divisibles_por_4 += 1

    elif numero_aleatorio % 8 == 0:
        numeros_divisibles_por_8 += 1

    #SEGUNDO PUNTO
    if numero_aleatorio > 2000:
        numeros_mayores_2000 += 1

    #TERCER PUNTO
    if numero_aleatorio < primer_valor_generado:
        numeros_menores_primer_valor_generado += 1

    #CUARTO PUNTO
    if numero_aleatorio == 1:
        print('El número 1 apareció')


    if numero_aleatorio == 2500:
        print('El número 2500 apareció')





promedio_num_may_2000 = 1000 // numeros_mayores_2000
promedio_num_menores_al_primero = 1000 // numeros_menores_primer_valor_generado

print(f'Los números que son divisibles por 4 y por 8 son: {numeros_divisibles_por_4_y_por_8}')
print(f'Los números que son divisibles por 4 y no por 8 son: {numeros_divisibles_por_4_pero_no_8}')
print(f'Los números que son divisibles solamente por 4 son: {numeros_divisibles_por_4}')
print(f'Los números que son divisibles solamente por 8 son: {numeros_divisibles_por_8}')
print(f'El promedio de los números mayores a 2000 es: {promedio_num_may_2000}%')
print(f'La cant de números menores la primero que salió fue: {numeros_menores_primer_valor_generado}')
print(f'El promedio de números menores al primero es: {promedio_num_menores_al_primero}%')




