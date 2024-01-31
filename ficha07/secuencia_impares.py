primer_numero = int(input('Ingrese el número inicial: '))
segundo_numero = int(input('Ingrese el número final: '))


if primer_numero < segundo_numero:
    menor, mayor = primer_numero, segundo_numero
else:
    menor, mayor = segundo_numero, primer_numero

if menor % 2 == 0:
    menor += 1
if mayor % 2 == 0:
    mayor -= 1

print('Secuencia ascendente: ')
ascend = range(menor, mayor + 1, 2)
for num in ascend:
    print(num, end=' | ')

print('\nSecuencia descendente: ')
descend = range(mayor, menor - 1, 2)
for num in descend:
    print(num, end=' | ')
