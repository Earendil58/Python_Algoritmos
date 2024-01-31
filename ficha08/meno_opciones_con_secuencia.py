

print('Ingrese alguna de las siguientes opciones: ')
print('a) Dada la serie de números naturales desde 1 hasta n (n ingresado por teclado y validando que sea mayor a cero) mostrar la suma de los cuadrados')
print('b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales')
print('c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares')
print('d) Salir')

opcion = input('Su opción elegida es?: ')

opcion = opcion.upper()

while 'A' > opcion > 'D':
    print('Usted no ingresó una opción correcta')

    print('Ingrese alguna de las siguientes opciones: ')
    print('a) Dada la serie de números naturales desde 1 hasta n (n ingresado por teclado y validando que sea mayor a cero) mostrar la suma de los cuadrados')
    print('b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales')
    print('c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares')
    print('d) Salir')

    opcion = input('Su opción elegida es?: ')


if opcion == 'A':
    n = int(input('Ingrese el margen derecho de la secuencia numérica: '))
    acumulador_cuadrados = 0


    for i in range(1, n + 1):
        acumulador_cuadrados += i**2

    print(f'El rango ingresado fue: {(1,n)} y la suma de los cuadrados de su secuencia numérica fue de: {acumulador_cuadrados}')

elif opcion == 'B':
    texto = input('Ingrese el texto, finaliza con un "." : ')
    vocales = 'aeiouAEIOU'
    palabra_contiene_vocal = 0
    caracter_anterior = ''

    for letra in texto:
        if letra == ' ' or letra == '.' or letra == ',':
            if caracter_anterior in vocales:
                palabra_contiene_vocal += 1
        caracter_anterior = letra

    print(f'La cantidad de palabras que contienen vocales, son: {palabra_contiene_vocal}')


elif opcion == 'C':
    valores_positivos = 0
    valores_negativos = 0

    numero_ingresado = float(input('Ingrese un número: '))

    while numero_ingresado != 0:
        if numero_ingresado > 0:
            valores_positivos += 1
        else:
            valores_negativos += 1

        numero_ingresado = float(input('Ingrese un número: '))

    print(f'Los valores ingresados fueron: {valores_negativos, valores_positivos}')

    if valores_positivos > valores_negativos:
        print(f'Los valores positivos, son mayoria.')

    elif valores_negativos > valores_positivos:
        print(f'Los valores negativos, son mayoria.')

    else:
        print('La cantidad de valores ingresados, es igual.')


elif opcion == 'D':
    print('Hasta luego!')



