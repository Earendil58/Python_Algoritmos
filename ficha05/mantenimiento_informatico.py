pc_id_uno = float(input('Ingrese el Id de su Pc_1: '))
tiempo_repa_minutos_uno = int(input('Ingrese tiempo de repa, en minutos: '))
causa_mantenimiento_uno = int(input('Ingrese 1) si el problema es de Hardware o 2) si es de Software: '))

print('*-*-*-' * 20)

pc_id_dos = float(input('Ingrese el Id de su Pc_2: '))
tiempo_repa_minutos_dos = int(input('Ingrese tiempo de repa, en minutos: '))
causa_mantenimiento_dos = int(input('Ingrese 1) si el problema es de Hardware o 2) si es de Software: '))

print('*-*-*-' * 20)

pc_id_tres = float(input('Ingrese el Id de su Pc_3: '))
tiempo_repa_minutos_tres = int(input('Ingrese tiempo de repa, en minutos: '))
causa_mantenimiento_tres = int(input('Ingrese 1) si el problema es de Hardware o 2) si es de Software: '))

print('*-*-*-' * 20)

tiempo_total_mantenimiento = tiempo_repa_minutos_uno + tiempo_repa_minutos_dos + tiempo_repa_minutos_tres

tiempo_repa_mayor = ''

if tiempo_repa_minutos_uno > tiempo_repa_minutos_dos and tiempo_repa_minutos_uno > tiempo_repa_minutos_tres:
    tiempo_repa_mayor = tiempo_repa_minutos_uno

elif tiempo_repa_minutos_dos > tiempo_repa_minutos_uno and tiempo_repa_minutos_dos > tiempo_repa_minutos_tres:
    tiempo_repa_mayor = tiempo_repa_minutos_dos

else:
    tiempo_repa_mayor = tiempo_repa_minutos_tres

tiempo_promedio_mantenimiento = (tiempo_repa_minutos_uno + tiempo_repa_minutos_dos + tiempo_repa_minutos_tres ) / 3

if causa_mantenimiento_uno == 1 and causa_mantenimiento_dos == 1 and causa_mantenimiento_tres == 1:
    print('Todas tuvieron problema de Hardware')

print(f'El tiempo total de reparación de las 3 \
fue de: {tiempo_total_mantenimiento} minutos, \
el tiempo promedio de reparación fue de: {tiempo_promedio_mantenimiento} minutos')

print(f'La que más tiempo demoró en repararse fue: {tiempo_repa_mayor}')


