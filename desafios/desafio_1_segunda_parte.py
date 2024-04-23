horas = int(input('Ingrese la cantidad de horas: '))
minutos = int(input('Ingrese la cantidad de minutos: '))
segundos = int(input('Ingrese la cantidad de segundos: '))

horas_a_segundos = horas * 60 * 60
minutos_a_segundos = minutos * 60

cant_total_en_segundos = horas_a_segundos + minutos_a_segundos + segundos

print(cant_total_en_segundos)


