import random

random.seed(20220512)

contador = 0

#PUNTO 1
numeros_multiplos_3 = 0
numeros_multiplos_5_pero_no_3 = 0
numeros_que_no_cumplen_lo_anterior = 0

#PUNTO 2
numero_mayor_que_comienza_con_1 = 0

#PUNTO 3
sumatoria_numeros_pares_y_multiplos_11 = 0
conteo_numeros_pares_y_multiplos_11 = 0

#PUNTO 4
porcentaje_numeros_multiplos_3 = 0
porcentaje_numeros_multiplos_5_pero_no_3 = 0
porcentaje_numeros_que_no_cumplen_lo_anterior = 0


while contador < 25000:
    contador += 1
    num_aleatorio = random.randint(1,45000)

    #LOGICA PUNTO 1
    if ((num_aleatorio % 5) != 0) and ((num_aleatorio % 3) != 0):
        numeros_que_no_cumplen_lo_anterior += 1

    if ((num_aleatorio % 5) == 0) and ((num_aleatorio % 3) != 0):
        numeros_multiplos_5_pero_no_3 += 1

    if ((num_aleatorio % 3) == 0):
        numeros_multiplos_3 += 1

    #LOGICA PUNTO 2
    cadena_num_aleatorio = str(num_aleatorio)
    if cadena_num_aleatorio[0] == '1':
        if num_aleatorio > numero_mayor_que_comienza_con_1:
            numero_mayor_que_comienza_con_1 = num_aleatorio

    #PUNTO 3
    if ((num_aleatorio % 2) == 0) and ((num_aleatorio % 11) == 0):
        sumatoria_numeros_pares_y_multiplos_11 += num_aleatorio
        conteo_numeros_pares_y_multiplos_11 += 1



#PUNTO 3 TMB
promedio_numeros_pares_y_multiplos_11 = (sumatoria_numeros_pares_y_multiplos_11) // conteo_numeros_pares_y_multiplos_11

#PUNTO 4

porcentaje_numeros_multiplos_3 = (numeros_multiplos_3 * 100) // 25000
porcentaje_numeros_multiplos_5_pero_no_3 = (numeros_multiplos_5_pero_no_3 * 100) // 25000
porcentaje_numeros_que_no_cumplen_lo_anterior = (numeros_que_no_cumplen_lo_anterior * 100) // 25000



#PRINT PUNTO 1
print(f'La cant de números multiplos de 3 son: {numeros_multiplos_3}')
print(f'La cant de números múltiplos de 5 pero no de 3, son: {numeros_multiplos_5_pero_no_3}')
print(f'La cant de números que no cumplen con ninguna de las anteriores condiciones son: {numeros_que_no_cumplen_lo_anterior}')


#PRINT PUNTO 2
print(f'El mayor número que empieza con 1 es: {numero_mayor_que_comienza_con_1}')

#PRINT PUNTO 3
print(f'El promedio de los números generados que son pares y múltiplos de 11, es: {promedio_numeros_pares_y_multiplos_11}')

#PRINT PUNTO 4
print(f'El porcentaje de los múltiplos de 3, sobre el total de los números generados es de: {porcentaje_numeros_multiplos_3}%')
print(f'El porcentaje de números múltiplos de 5 pero no de 3, sobre el total de los números generados es de: {porcentaje_numeros_multiplos_5_pero_no_3}%')
print(f'El porcentaje de los números que no cumplen ninguna de las condiciones anteriores, sobre el total de los números generados es de: {porcentaje_numeros_que_no_cumplen_lo_anterior}%')




