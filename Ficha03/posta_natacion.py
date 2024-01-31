
#TIEMPO TOTAL A CENTESIMAS
espalda = 52 * 100 + 15
pecho = 62 * 100 + 75
mariposa = 59 * 100 + 80
libre = 48 * 100 + 15

tiempo_total_centesimas = espalda + pecho + mariposa + libre

tiempo_total_minutos = tiempo_total_centesimas // 6000
resto = tiempo_total_centesimas % (6000 * tiempo_total_minutos)

tiempo_total_segundos = resto // 100
tiempo_en_centesimas = resto % 100




print('tiempo en centesimas: ', tiempo_total_centesimas)
print('tiempo en minutos',      tiempo_total_minutos)
print('tiempo en segundos',     tiempo_total_segundos)
print('tiempo en centesimas: ', tiempo_en_centesimas)

