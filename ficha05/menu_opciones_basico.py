from math import sqrt

print('Ingrese los lados a calcular: ')

print('-' * 30)

a = int(input('Ingrese el lado a: '))
b = int(input('Ingrese el lado b: '))
c = int(input('Ingrese el lado c: '))

print('Ingrese la opción del cálculo que desea realizar: ')

print('-' * 30)

print('1)Calcular la superficie de un triangulo? ')
print('2)Calcular el perímetro de un triangulo? ')
print('3)Verificar cual fue el lado menor? ')

opc = int(input('Ingrese la opción elegida: '))

s = (a + b + c) / 2

if opc == 1:
    superficie = sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'Su opción elegida fue la: {opc} y la sup de un triangulo es: {superficie}')

elif opc == 2 :
    perimetro = a + b + c
    print(f'La opción elegida fue la: {opc} y el perímetro de un triangulo es: {perimetro}')

elif opc == 3:
    menor = ''
    if a < b and a < c:
        menor = a
    elif b < a and b < c:
        menor = b
    else:
        menor = c
    print(f'La opción elegida fue: {opc} y el lado menor es: {menor}')

else:
    print('Usted no ingresó una opción válida, recuerde que las opciones son 1,2 o 3')

