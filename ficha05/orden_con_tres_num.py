n1 = int(input('Ingrese el primer número: '))
n2 = int(input('Ingrese el segundo número: '))
n3 = int(input('Ingrese el tercer número: '))

mayor = ''
medio = ''
menor = ''

if n1 > n2 and n1 > n3:
    mayor = n1
    if n2 > n3:
        medio = n2
        menor = n3
    else:
        medio = n3
        menor = n2

if n2 > n1 and n2 > n3:
    mayor = n2
    if n1 > n3:
        medio = n1
        menor = n3
    else:
        medio = n3
        menor = n1
if n3 > n1 and n3 > n2:
    mayor = n3
    if n1 > n2:
        medio = n1
        menor = n2
    else:
        medio = n2
        menor = n1


if (mayor % medio) == menor:
    print(f'El menor es el resto de la división del mayor y el del medio')

print(f'Los valores, en orden descendente son: {mayor}, {medio}, {menor}')

