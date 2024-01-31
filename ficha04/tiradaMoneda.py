import random

eleccion_moneda = input('Elija "cara" o "cruz": ')
moneda = random.choice(['cara', 'seca'])


if eleccion_moneda == moneda:
    print(f'El jugador acertó, salió {moneda} y el jugador había elegido: {eleccion_moneda}')
else:
    print(f'El jugador no acertó, salió {moneda} y el jugador había elegido {eleccion_moneda}')
