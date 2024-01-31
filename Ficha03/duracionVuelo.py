TIEMPO_TAXI = 45

print('Determinacion de tiempo de llegada a aeropuerto')
print('Las horas se ingresaran en formato hh:mm (ejemplo: 14:45 o 05:30)')

horario_partida = input('Ingrese el horario de partida: ')
horario_llegada = input('Ingrese el horario de llegada: ')

#EXTRACCION TIEMPO DE PARTIDA
hp = horario_partida[0] + horario_partida[1]
hp = int(hp)
mp = horario_partida[3] + horario_partida[4]
mp = int(mp)

horario_partida_minutos = (hp*60) + mp

#EXTRACCION TIEMPO DE LLEGADA
hl = horario_llegada[0] + horario_llegada[1]
hl = int(hl)
ml = horario_llegada[3] + horario_llegada[4]
ml = int(ml)

horario_llegada_minutos = (hl*60) + ml

#TIEMPO TOTAL DE VUELO EN MINUTOS
tiempo_vuelo =  horario_llegada_minutos - horario_partida_minutos

print('El tiempo total de vuelo, en minutos, fue: {}'.format(tiempo_vuelo))








