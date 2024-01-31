import random

numero_aleatorio =  random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),\
                    random.randint(1,100), random.randint(1,100),random.randint(1,100),random.randint(1,100),\
                    random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),\
                    random.randint(1,100),random.randint(1,100),random.randint(1,100)


a = int(input('Ingrese el 1er número (un valor ente 1 y 100): '))
b = int(input('Ingrese el 2er número (un valor ente 1 y 100): '))
c = int(input('Ingrese el 3er número (un valor ente 1 y 100): '))

if a in numero_aleatorio or b in numero_aleatorio or c in numero_aleatorio:
    print('El jugador marcó algún número en la tarjeta')

else:
    print('El jugador tiene mala suerte, no marcó ningún número')


print('La tarjeta es: {}'.format(numero_aleatorio))
