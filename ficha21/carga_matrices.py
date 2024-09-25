
arreglo = []

for i in range(3):
    arreglo.append([])
    for j in range(3):
        arreglo[i].append(None)

print(arreglo)

## ------------------------------------------------------------------------------------------------------------------------

arreglo_1 = [0] * 3
for j in range(3):
    arreglo_1[j] = [0] * 3

print(arreglo_1)

## ------------------------------------------------------------------------------------------------------------------------

arreglo_2 = [[1] * 3 for f in range(3)]

print(arreglo_2)

## ------------------------------------------------------------------------------------------------------------------------

matriz = [['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'i']]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])

filas, columnas = 3, 4

matriz_pre_formada = [[0] * columnas for i in range(filas)]

print(matriz_pre_formada)

## ------------------------------------------------------------------------------------------------------------------------

for i in range(filas):
    for j in range(columnas):
        matriz_pre_formada[i][j] = input(f'Ingrese el elemento: {i + 1, j + 1} de la matriz: ')

print(matriz_pre_formada)

## ------------------------------------------------------------------------------------------------------------------------

# carga por teclado... por columnas en orden creciente...
filas, columnas = 3, 4
m6 = [[0] * columnas for f in range(filas)]
for c in range(columnas):
    for f in range(filas):
        m6[f][c] = int(input('Valor: '))
print('Matriz 6 leida:', m6)

