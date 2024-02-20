lista = [47, 17, 14, 41, 37, 74, 48]

print(f'Lista original: {lista}')

lista[2:5] = [10,20,30]
print(f'Lista modificada 1: {lista}')

lista[1:4] = []
print(f'Lista modificada 2: {lista}')

lista[2:2] = [90]
print(f'Lista modificada 3: {lista}')

lista[:0] = lista
print(f'Lista modificada 4: {lista}')

lista[len(lista):] = [100]
print(f'Lista modificada 5: {lista}')

sublista_11 = lista[2:-1]
print(f'Sublista 1: {sublista_11}')

sublista_12 = 2 * lista[2:5]
print(f'Sublista 2: {sublista_12}')
