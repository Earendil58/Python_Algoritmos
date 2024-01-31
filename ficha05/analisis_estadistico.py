a = float(input('Ingrese el primer valor: '))
b = float(input('Ingrese el segundo valor: '))
c = float(input('Ingrese el tercer valor: '))

mayor = None
restantes = None

if a % 5 == 0 or b % 5 == 0 or c % 5 == 0:
    print('Alguno de los números es múltiplo de 5')

if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print(f'Todos ellos son impares: {a}, {b}, {c}')

if a > b and a > c:
    mayor = a
    restantes = b + c
elif b > c :
    mayor = b
    restantes = a + c
else:
    mayor = c
    restantes = a + b

if mayor > restantes:
    print(f'El mayor de ellos ({mayor}) supera a los otros dos')
