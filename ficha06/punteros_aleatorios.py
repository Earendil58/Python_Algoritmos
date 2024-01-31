import random

random.seed(37)

print('Ingrese alguna de las siguiente opciones: ')

print('1) Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000]')
print('2) Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000]')
print('3) Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y calcular el valor promedio de los números menores a 10.000')

opcion = int(input('Ingrese la opción elegida: '))

while 0 < opcion < 4:

    if opcion == 1:
        conteo = 0
        acumulador_de_aleatorios = 0

        while conteo < 1000:
            conteo += 1
            numero_aleatorio = random.randint(1,100_000)
            acumulador_de_aleatorios += numero_aleatorio

        promedio = round((acumulador_de_aleatorios / 1000),2)
        print(f'El promedio de los 1000 nros aleatorios generados es de : {promedio}')

    elif opcion == 2:
        mayor = 0
        conteo = 0


        while conteo < 10_000:
            conteo += 1
            num_aleatorio = random.randint(0,100_000)

            if num_aleatorio > mayor:
                mayor = num_aleatorio

        print(f'El mayor de 10.000 números aleatorios generados, es el: {mayor}')

    elif opcion == 3:
        menor = 100_000
        conteo = 0
        num_menores_10000 = 0
        conteo_num_menores_10000 = 0


        while conteo < 5000:
            conteo += 1
            num_aleatorio = random.randint(0,100_000)

            if num_aleatorio < 10_000:
                num_menores_10000 += num_aleatorio
                conteo_num_menores_10000 += 1

            if num_aleatorio < menor:
                menor = num_aleatorio

            if conteo_num_menores_10000 != 0:
                promedio_num_menore_10000 = round((num_menores_10000 / conteo_num_menores_10000),2)

        print(f'El menor de 5000 números aleatorios generados fue el: {menor}')
        print(f'El promedio de los números menores que 10000 es de: {promedio_num_menore_10000}')


    print('Ingrese alguna de las siguiente opciones: ')
    print('1) Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000]')
    print('2) Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000]')
    print('3) Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y calcular el valor promedio de los números menores a 10.000')

    opcion = int(input('Ingrese la opción elegida: '))

print('Fin del programa')
