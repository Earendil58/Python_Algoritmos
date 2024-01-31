
primer_competidor_nombre = input('Ingrese el nombre del primer competidor: ')
primer_competidor_tiempo = input('Ingrese el tiempo del primer competidor, en formato (hh:mm:ss):  ')

segundo_competidor_nombre = input('Ingrese el nombre del segundo competidor: ')
segundo_competidor_tiempo = input('Ingrese el tiempo del segundo competidor, en formato (hh:mm:ss):  ')

tercer_competidor_nombre = input('Ingrese el nombre del tercer competidor: ')
tercer_competidor_tiempo = input('Ingrese el tiempo del tercer competidor, en formato (hh:mm:ss):  ')


#PASO A SEGUNDOS TIEMPO PRIMER COMPETIDOR


primer_competidor_tiempo_horas = int(primer_competidor_tiempo[0:2])
primer_competidor_tiempo_minutos = int(primer_competidor_tiempo[3:5])
primer_competidor_tiempo_segundos = int(primer_competidor_tiempo[6:8])

if primer_competidor_tiempo_horas < 10:
    primer_competidor_tiempo_horas[0] = 0

if primer_competidor_tiempo_minutos < 10:
    primer_competidor_tiempo_minutos[0] = 0

