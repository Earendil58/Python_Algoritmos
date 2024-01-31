aguinaldo = 0
sueldo_mas_bajo = 0
sueldo_mas_alto = 0
sumatoria_sueldo = 0

semestre = ('Enero', 'Febrero', 'Marzo', 'Abril','Mayo', 'Junio')


for mes in semestre:
    sueldo = int(input(f'Ingrese el sueldo de {mes}:'))
    sumatoria_sueldo += sueldo

    #me aseguro que se compute el primero como el mas bajo para ser usado para comparar
    if mes == 'Enero' or sueldo < sueldo_mas_bajo:
        sueldo_mas_bajo = sueldo

    #Calculo el sueldo mas alto, para el aguinaldo
    if sueldo > sueldo_mas_alto:
        sueldo_mas_alto = sueldo



aguinaldo = sueldo_mas_alto / 2
sueldo_promedio = sumatoria_sueldo / 6
print(f'El aguinaldo es de: ${aguinaldo}')
print(f'El sueldo más alto fue de: ${sueldo_mas_alto}')
print(f'El sueldo más bajo fue de: ${sueldo_mas_bajo}')
print(f'El sueldo promedio fue de: {sueldo_promedio}')




