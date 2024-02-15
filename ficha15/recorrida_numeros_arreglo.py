numeros = []

for i in range(1,11):
    numeros.append(i)

print(f'Los números del arreglo original son: {numeros}')


for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(f'Los números pares son: {numeros[i]}')
