frente = float(input('Ingrese la medida de frente del terreno: '))
fondo = float(input('Ingrese la medida de fondo del terreno: '))


superficie = frente * fondo

if frente==fondo:
    print('El terreno es cuadrado')

else:
    print('El terreno es rectangular')

print('El terreno tiene una sup. de:{} , mts2'.format(superficie))
