
# arreglo = []
#
# for i in range(3):
#     arreglo.append([])
#     for j in range(3):
#         arreglo[i].append(None)
#
# print(arreglo)
#
#
# arreglo_1 = [0] * 3
# for j in range(3):
#     arreglo_1[j] = [0] * 3
#
# print(arreglo_1)
#
#
# arreglo_2 = [[1] * 3 for f in range(3)]
#
# print(arreglo_2)

matriz = [['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'i']]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])



