print('Observatorio Metereologico')
print('=' * 80)

#entrada de datos
temp1 = int(input('Ingrese la primer temperatura del dia: '))
temp2 = int(input('Ingrese la segunda temperatura del dia: '))
temp3 = int(input('Ingrese la tercer temperatura del dia: '))
temp4 = int(input('Ingrese la cuarta temperatura del dia: '))

temp_max = ''
temp_min = ''

promedio_diaria = (temp1 + temp2 + temp3 + temp4) / 4

if temp1 > temp2 and temp1 > temp3 and temp1 > temp4:
    temp_max = temp1
    if temp2 < temp3 and temp2 < temp4:
        temp_min = temp2
    elif temp3 < temp2 and temp3 < temp4:
        temp_min = temp3
    else:
        temp_min = temp4

elif temp2 > temp1 and temp2 > temp3 and temp2 > temp4:
    temp_max = temp2
    if temp1 < temp3 and temp1 < temp4:
        temp_min = temp1
    elif temp3 < temp1 and temp3 < temp4:
        temp_min = temp3
    else:
        temp_min = temp4

elif temp3 > temp1 and temp3 > temp2 and temp3 > temp4:
    temp_max = temp3
    if temp1 < temp2 and temp1 < temp4:
        temp_min = temp1
    elif temp2 < temp1 and temp2 < temp4:
        temp_min = temp2
    else:
        temp_min = temp4

else:
    temp_max = temp4
    if temp1 < temp2 and temp1 < temp3 and temp1 < temp4:
        temp_min = temp1
    elif temp2 < temp1 and temp2 < temp3:
        temp_min = temp2
    else:
        temp_min = temp3



if temp1 > promedio_diaria or temp2 > promedio_diaria or temp3 > promedio_diaria or temp4 > promedio_diaria:
    print(f'Alguna de las temperaturas es mayor al promedio que es de: {promedio_diaria}')

print(f'La temp max es: {temp_max} y la temp min es: {temp_min}')


