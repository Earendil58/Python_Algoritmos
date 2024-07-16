lista_01 = [1,2,3,4,5,6,7,8,9,10]

print(f'Lista-01: {lista_01}')

lista_02 = lista_01[1:4]

print(f'Lista-02: {lista_02}')

lista_01[2:5] = [6,8,10]

print(f'Nueva lista-01: {lista_01}')

lista_01[2:5] = []

print(f'Nueva lista-01-02: {lista_01}')

lista_01[2:2] = [66]

print('Nuevo valor de lista-01',lista_01, sep=' --> ')

lista_01[:0] = lista_01

print(f'Inserta nuevo valor de si mismo al principio: {lista_01}')

lista_01[len(lista_01):] = [100]

print(f'Agrega un elemento al final de la lista: {lista_01}')
