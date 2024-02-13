notas = []

for i in range(4):
    nota = int(input('Ingrese su nota: '))
    notas.append(nota)

print(f'Sus notas fueron: {notas}')

suma = 0

for i in range(len(notas)):
    suma += notas[i]

promedio = suma / len(notas)

print(f'Su promedio es de: {promedio}')


