import random

vueltas = 0
mayor = -100001
numeros_positivos = 0

while vueltas < 10000:
    vueltas += 1

    n = random.randint(-100000,100000)

    if n > mayor:
        mayor = n

    if n > 0:
        numeros_positivos += 1


porcentaje_numeros_positivos_sobre_total = round((numeros_positivos * 100) / vueltas, 2)

print(f'El mayor número entre [-100_000, 100_000], fue: {mayor}')
print(f'El porcentaje de números positivos sobre el total de números que se contabilizaron fue de: {porcentaje_numeros_positivos_sobre_total}%')
print(f'Las vueltas contabilizadas fueron: {vueltas}')
