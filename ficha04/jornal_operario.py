turno_trabajado = int(input('Ingrese el código del turno trabajado, 1 para diurno, 2 para nocturno: '))
horas_trabajadas = float(input('Ingrese la cantidad de horas trabajadas: '))

if turno_trabajado == 1:
    monto = horas_trabajadas * 35.5
else:
    monto = horas_trabajadas * 40.6

print(f'El monto por el turno de trabajo y las horas es: {monto}')
