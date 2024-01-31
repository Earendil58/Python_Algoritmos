from math import sqrt

print('Programa controlado por menu de opciones:')

print('1)Cargar un valor entero n por teclado, y obtener la suma de los enteros del 1 al n.')
print('2)Cargar un valor entero n por teclado, y obtener su factorial.')
print('3)Cargar por teclado los coeficientes a, b, y c de un polinomio de segundo grado, y obtener el '
      'valor del polinomio en el punto x, siendo x un valor que también se carga por teclado.')

opcion = int(input('Ingrese una de las opciones mencionadas: '))

while opcion < 0:
    opcion = int(input('Ingrese una de las opciones mencionadas: '))
    if opcion < 0:
        print('Ingrese un número dentro de las opciones mencionadas')

if opcion == 1:
    print('Usted eligió la opción 1')
    n = int(input('Ingrese un entero: '))
    sumatorio = 0

    for i in range(1,n + 1):
        sumatorio += i

    print(f'El sumatorio de los números del 1 a {n} es: {sumatorio}')


elif opcion == 2:
    print('Usted eligió la opción 2')
    n = int(input('Ingrese un entero: '))
    sumatorio = 1

    for i in range(1, n + 1):
        sumatorio *= i

    print(f'El factorial de los números de 1 a {n} es: {sumatorio}')


elif opcion == 3:
    print('Usted eligió la opción 3')
    a = int(input('Ingrese el coeficiente "a": '))
    b = int(input('Ingrese el coeficiente "b": '))
    c = int(input('Ingrese el coeficiente "c": '))
    x = int(input('Ingrese un valor para el punto "x": '))

    discriminante = sqrt((b**2) - (4*a*c))

    if a > 0 and discriminante >= 0:
        raiz_x1 = (-b + discriminante) / (2 * a)
        raiz_x2 = (-b - discriminante) / (2 * a)

        print(f'Las raices del polinomio, para los coeficientes a:{a}, b:{b}, c:{c}, en el punto x: {x} es: raiz_x1: {raiz_x1} y raiz_x2: {raiz_x2}')

    else:
        print(f'No está definida la función para los coeficientes a:{a}, b:{b}, c:{c}, en el punto x: {x}')

