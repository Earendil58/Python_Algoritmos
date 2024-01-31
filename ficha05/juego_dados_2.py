import random

dado_numeros_posibles = (1,2,3,4,5,6)
campeon = float(input('Ingrese el record del campeon: '))

puntos_uno = puntos_dos = 0
dado_mayor_valor_ronda_dos = dado_menor_valor_ronda_dos = -1

# PRIMERA RONDA
jugador_uno_primera_ronda = random.choice(dado_numeros_posibles)
jugador_dos_primera_ronda = random.choice(dado_numeros_posibles)

puntaje_primera_ronda = jugador_uno_primera_ronda + jugador_dos_primera_ronda

# SEGUNDA RONDA
jugador_uno_segunda_ronda = random.choice(dado_numeros_posibles)
jugador_dos_segunda_ronda = random.choice(dado_numeros_posibles)

puntaje_segunda_ronda = jugador_uno_segunda_ronda + jugador_dos_segunda_ronda

if jugador_uno_segunda_ronda > jugador_dos_segunda_ronda:
    dado_mayor_valor_ronda_dos = jugador_uno_segunda_ronda

else:
    dado_mayor_valor_ronda_dos = jugador_dos_segunda_ronda


#LOGICA PRIMERA RONDA
if puntaje_primera_ronda % 2 == 0:
    puntos_dos = puntaje_primera_ronda
else:
    puntos_uno = puntaje_primera_ronda


#LOGICA SEGUNDA RONDA
if puntaje_segunda_ronda % 2 == 0:
    puntos_uno -= dado_menor_valor_ronda_dos
    puntos_dos += dado_mayor_valor_ronda_dos
else:
    puntos_uno += dado_mayor_valor_ronda_dos
    puntos_dos -= dado_menor_valor_ronda_dos


print(f'Los puntos del jugador 1 fueron: {puntos_uno}')
print(f'Los puntos del jugador 2 fueron: {puntos_dos}')


if puntos_uno > campeon:
    print(f'El jugador uno ganó al campeón: puntos_1:{puntos_uno} vs ex_campeon: {campeon}')

elif puntos_dos > campeon:
    print(f'El jugador dos ganó al campeón: puntos_2:{puntos_dos} vs ex_campeon: {campeon}')

else:
    print(f'Ninguno de los dos jugadores venció al campeón: {campeon}')



