import random

TARIFA_ESTANDAR = 90
TARIFA_PROMOCIONAL = 50
costo = 0


numero_aleatorio = random.randint(0,9)

patente = (input('Ingrese los digitos de su patente: '))

print('El número que salió sorteado es: {}'.format(numero_aleatorio))

if patente[-1]==7:
    if patente==numero_aleatorio:
        costo=TARIFA_PROMOCIONAL*0.5
    else:
        costo=TARIFA_PROMOCIONAL*0.1

else:
    if patente==numero_aleatorio:
        costo=TARIFA_PROMOCIONAL
    else:
        costo=TARIFA_ESTANDAR


print('El costo es: {}'.format(costo))
