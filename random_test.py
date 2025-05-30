dinero = int(input("Digite o valor do dinero: "))

cant_500 = cant_200 = cant_100 = cant_50 = cant_20 = cant_10 = cant_2 = cant_1 = 0
sobrante = 0

cant_500 = dinero // 500
sobrante = dinero % 500

if sobrante > 200:
    cant_200 = sobrante // 200
    sobrante = sobrante % 200

if sobrante > 100:
    cant_100 = sobrante // 100
    sobrante = sobrante % 100

if sobrante > 50:
    cant_50 = sobrante // 50
    sobrante = sobrante % 50

if sobrante > 20:
    print('entro en 20')
    cant_20 = sobrante // 20
    sobrante = sobrante % 20

if sobrante > 10:
    cant_10 = sobrante // 10
    sobrante = sobrante % 10

if sobrante > 2:
    cant_2 = sobrante // 2
    sobrante = sobrante % 2

if sobrante > 1:
    cant_1 = sobrante // 1

print(f'''
        El dinero que usted ingresó es de: {dinero}
        'La cant de billetes de $500 es de: {cant_500}
        'La cant de billetes de $200 es de: {cant_200}
        'La cant de billetes de $100 es de: {cant_100}
        'La cant de billetes de $50 es de: {cant_50}
        'La cant de billetes de $20 es de: {cant_20}
        'La cant de billetes de $10 es de: {cant_10}
        'La cant de billetes de $2 es de: {cant_2}
        'La cant de billetes de $1 es de: {cant_1}''')
