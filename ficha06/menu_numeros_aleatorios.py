import random


print('Elija alguna opción: ')
print('1) Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000]')
print('2) Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000]')
print('3) Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] '
      'y calcular el valor promedio de los números menores a 10.000')
print('otro) Salir del programa: ')

opcion = int(input('Su opción es: '))


while 1 <= opcion <= 3:

    if opcion == 1:
        acumulador = 0
        vuelta = 0
        while vuelta < 1000:
            numero = random.randint(0,100_000)
            acumulador += numero
            vuelta += 1

        promedio_1 = numero / vuelta
        print(f'El promedio de {vuelta} números aleatorios es: {promedio_1}')


    elif opcion == 2:
        numero = random.randint(0,100_000)
        vuelta = 0
        mayor = -1

        while vuelta < 10000:

            if numero > mayor:
                mayor = numero

            vuelta += 1
        print(f'El mayor número de {vuelta} es: {mayor}')


    elif opcion == 3:
        numero = random.randint(0,100_000)
        vuelta = 0
        menor = 100_001
        num_menores_diezmil = 0


        while vuelta < 5000:
            if numero < menor:
                menor = numero

            if numero < 10_000:
                num_menores_diezmil += 1

            vuelta += 1

        promedio_num_menores_diezmil = (num_menores_diezmil / 5000)
        print(f'El menor número de {vuelta} números aleatorios es: {menor}')
        print(f'El promedio de números menores a 10.000 es {promedio_num_menores_diezmil}%')



    print('-'*80)
    print('Elija alguna opción: ')
    print('1) Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000]')
    print('2) Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000]')
    print('3) Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] '
            'y calcular el valor promedio de los números menores a 10.000')
    print('otro) Salir del programa: ')

    opcion = int(input('Su opción es: '))

print('Fin del programa')
