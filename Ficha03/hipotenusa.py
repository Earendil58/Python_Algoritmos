from math import sqrt

lado_a = float(input('Ingrese el valor del lado A: '))
lado_b = float(input('Ingrese el valor del lado B: '))


if lado_a > lado_b:
    lado_mayor = [lado_a, 'Lado A']
else:
    lado_mayor = [lado_b, 'Lado B']

hipotenusa = round(sqrt((lado_a **2 + lado_b ** 2)), 2)

print(f'El lado más grande es {lado_mayor} y el valor de la hipotenusa es {hipotenusa}')
