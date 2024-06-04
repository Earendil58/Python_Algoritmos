semestre = 6
sueldo = 0
sueldo_mayor = 0
mes_sueldo_mayor = 0
sueldo_menor = None
mes_sueldo_menor = None
sumatoria_sueldos = 0
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octobre', 'Noviembre', 'Diciembre']

for mes in range(semestre):
    sueldo = float(input('Ingrese el sueldo correspodiente al mes: '))
    sumatoria_sueldos += sueldo

    if sueldo > sueldo_mayor:
        sueldo_mayor = sueldo
        mes_sueldo_mayor = mes

    if sueldo_menor is None:
        sueldo_menor = sueldo

    if sueldo < sueldo_menor:
        sueldo_menor = sueldo
        mes_sueldo_menor = mes




aguinaldo = sueldo_mayor / 2
promedio_sueldo = sumatoria_sueldos / semestre


print(f'El aguinaldo es de: ${aguinaldo}')
print(f'El monto más alto percenece al mes de: {meses[mes_sueldo_mayor]}')
print(f'El sueldo menor se recibió en el mes: {meses[mes_sueldo_menor]}')
print(f'El promedio de los sueldos obtenidos en el semestre es de : {promedio_sueldo}')
