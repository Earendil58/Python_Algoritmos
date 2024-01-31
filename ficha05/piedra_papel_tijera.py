import random

#ELIJE COMPU
opciones_computadora = ['piedra', 'papel', 'tijera']
eleccion_computadora = random.choice(opciones_computadora)

#ELIJE JUGADOR
eleccion_jugador = input('Ingrese una opción entre PIEDRA, PAPEL, TIJERA: ')
eleccion_jugador =eleccion_jugador.lower()

ganador = ''

if eleccion_computadora == 'piedra':
    if eleccion_jugador == 'piedra':
        ganador = 'Empataron, ambos eligieron el mismo elemento'
    elif eleccion_jugador == 'papel':
        ganador = 'Gano el jugador'
    else:
        ganador = 'Gano la máquina'

elif eleccion_computadora == 'papel':
    if eleccion_jugador == 'piedra':
        ganador = 'Ganó la máquina'
    elif eleccion_jugador == 'papel':
        ganador = 'Empataron, ambos eligieron el mismo elemento'
    else:
        ganador = 'Ganó el jugador'

elif eleccion_computadora == 'tijera':
    if eleccion_jugador == 'tijera':
        ganador = 'Empataron, ambos eligieron el mismo elemento'
    elif eleccion_jugador == 'piedra':
        ganador = 'Ganó el jugador'
    else:
        ganador = 'Ganó la máquina'

print(f'La elección del jugador fue: {eleccion_jugador} y la elección de la computadora fue: {eleccion_computadora}')
print(f'El ganador fue: {ganador}')

