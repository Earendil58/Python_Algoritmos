import random

random.seed(76)
cant_numeros_pares_multiplos_6 = 0
primer_num_serie = 0
cant_numeros_mayores_que_primer_numero_de_serie_sin_incluirlo = 0


for i in range(5000):
    numero = random.randint(1,65_000)

    if numero % 6 == 0:
        cant_numeros_pares_multiplos_6 += 1

    if i == 0:
        primer_num_serie = numero

    if numero > primer_num_serie:
        cant_numeros_mayores_que_primer_numero_de_serie_sin_incluirlo += 1



porcentaje_numeros_mayores_que_primer_numero_de_serie_sin_incluirlo = round((cant_numeros_mayores_que_primer_numero_de_serie_sin_incluirlo * 100) / 5_000, 2)

print(f'La cant de num pares, multiplos de 6: {cant_numeros_pares_multiplos_6}')
print(f'El primer num de la serie es: {primer_num_serie}')
print(f'La cant de num mayores que el primer num de la serie, sin incluirlo, fueron: {cant_numeros_mayores_que_primer_numero_de_serie_sin_incluirlo}')
print(f'El porcentaje de los num mayores que el primer num de la seria, sin incluirlo, sobre el total de num fue de: {porcentaje_numeros_mayores_que_primer_numero_de_serie_sin_incluirlo}%')
