medida_frente = float(input('Ingresar la medida de frente del terreno: '))
medida_fondo = float(input('Ingresar la medida de fondo del terreno: '))

superficie = medida_frente * medida_fondo

if medida_frente == medida_fondo:
    print('El terreno es un cuadrado')
else:
    print('El terreno es un rectángulo')

print(f'La superficie es {superficie}')
