notas = []

for nota in range(4):
    nota = int(input('Ingrese una nota: '))
    notas.append(nota)


print(f'Las notas fueron: {notas}')


suma_notas = 0

print(len(notas))

for nota in range(len(notas)):
    suma_notas += notas[nota]


promedio = suma_notas / 4

print(f'El promedio es: {promedio}')



