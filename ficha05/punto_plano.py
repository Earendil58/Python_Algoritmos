from math import sqrt, asin

x = int(input('Ingrese el valor del punto x: '))
y = int(input('Ingrese el valor del punto y: '))


if x == 0 and y == 0:
    cuadrante = 'Alguno de los ejes o el origen'

elif x > 0 and y > 0:
    cuadrante = 'Primer cuadrante'

elif x < 0 and y > 0:
    cuadrante = 'Segundo cuadrante'

elif x < 0 and y < 0:
    cuadrante = 'Tercer cuadrante'

else:
    cuadrante = 'Cuarto cuadrante'


print(f'El cuadrante en el que están los puntos es: {cuadrante}')


