from math import sqrt

vueltas = int(input('Ingrese la cantidad de vueltas a iterar: '))

primer_cuadrante = 0
tercer_cuadrante = 0
mayor_distancia = 0
mayor_punto = ()

for i in range(vueltas):
    x = int(input('Ingrese un punto del eje x: '))
    y = int(input('Ingrese un punto del eje y: '))
    hipotenusa = sqrt( (x**2) + (y**2))

    #PRIMER CUADRANTE
    if x > 0 and y > 0:
        print(f'El punto, delimitado por {x} y {y}, se encuentra en el primer cuadrante')
        primer_cuadrante += 1

    #SEGUNDO CUADRANTE
    elif x < 0 and y > 0:
        print(f'El punto, delimitado por {x} y {y}, se encuentra en el segundo cuadrante')

    #TERCER CUADRANTE
    elif x < 0 and y < 0:
        print(f'El punto, delimitado por {x}, y {y}, se encuentra en el tercer cuadrante')
        tercer_cuadrante += 1

    #CUARTO CUADRANTE
    elif x > 0 and y < 0:
        print(f'El punto, delimitado por {x}, y {y}, se encuentra en el cuarto cuadrante')

    else:
        print(f'El punto, delimitado por {x}, y {y}, se encuentra en el limite entre cuadrantes')

    #MAYOR DIST A ORIGEN DE COORDENADAS
    hipotenusa = sqrt((x**2) + (y**2))
    if hipotenusa > mayor_distancia:
        mayor_distancia = hipotenusa
        mayor_punto = (x, y)



print(f'La cantidad de puntos en el primer cuadrante fueron: {primer_cuadrante}')
print(f'La cantidad de puntos en el tercer cuadrante fueron: {tercer_cuadrante}')
print(f'El punto con mayor distancia al origen fue: {mayor_punto}')
