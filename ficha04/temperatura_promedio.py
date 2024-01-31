temperatura_1 = float(input('Ingrese la primer temperatura: '))
temperatura_2 = float(input('Ingrese la segunda temperatura: '))
temperatura_3 = float(input('Ingrese la tercera temperatura: '))

promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3
mayor_promedio = ''

if temperatura_1 > promedio:
    mayor_promedio = temperatura_1
elif temperatura_2 > promedio:
    mayor_promedio = temperatura_2
else:
    mayor_promedio = temperatura_3

print(f'El promedio de temperaturas es: {promedio} y la temperatura que es mayor al promedio es: {mayor_promedio}')
