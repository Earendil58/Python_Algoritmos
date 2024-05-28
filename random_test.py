import random

print('Seleccione algunas de las siguientes opciones: ')
print('-' * 95)
print('Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].')
print('-' * 95)
print('Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].')
print('-' * 95)
print('''Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y 
          calcular el valor promedio de los números menores a 10.000.''')
print('-' * 95)
print('Cualquier otro número que ingrese, hará que salga de programa.')
print('-' * 95)

opcion = int(input('Ingrese algunas de las opciones anteriormente descriptas: '))

while 0 < opcion < 4:
    if opcion == 1:
        sumatorio = 0
        i = 0
        while i < 1000:
            i += 1
            numero_aleatorio = random.randint(0,100_000)
            sumatorio += numero_aleatorio

        promedio = sumatorio // i
        print(f'El promedio de los 1.000 números aleatorios generados en el rango de [0, 100.000], es: {promedio} ')


    elif opcion == 2:
        i = 0
        mayor = -0.1
        while i < 10_000:
            numero_aleatorio = random.randint(0,100_000)

            if numero_aleatorio > mayor:
                mayor = numero_aleatorio

            i+= 1

        print(f'El mayor de los números aleatorios entre [0,100.000] es: {mayor}')


    elif opcion == 3:
        i = 0
        menor = 100_001
        mayores_diezmil = 0
        mayores_diezmil_sumatorio = 0
        while i < 5000:
            numero_aleatorio = random.randint(0,100_000)

            if numero_aleatorio > 10000:
                mayores_diezmil += 1
                mayores_diezmil_sumatorio += numero_aleatorio

            if numero_aleatorio < menor:
                menor = numero_aleatorio

            i += 1
        print(f'El menor de los números aleatorios entre [0,100.000] es: {menor}')
        promedio_valores_diezmil = round(mayores_diezmil_sumatorio / mayores_diezmil, 2)
        print(f'El promedio de los números mayores a 10.000 es de : {promedio_valores_diezmil}')



    print()
    print()
    print('Seleccione algunas de las siguientes opciones: ')
    print('-' * 95)
    print('Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].')
    print('-' * 95)
    print('Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].')
    print('-' * 95)
    print('''Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y 
              calcular el valor promedio de los números menores a 10.000.''')
    print('-' * 95)
    print('Cualquier otro número que ingrese, hará que salga de programa.')
    print('-' * 95)
    opcion = int(input('Ingrese algunas de las opciones anteriormente descriptas: '))


print('Fin del programa')
