numeros = int(input('Ingresa la cantidad de numeros que deseas iterar: '))

segundo_menor: []
sumatoria_numeros_positivos = 0
contador_positivos = 0
mayor_numeros_negativos = 0

for num in range(numeros):
    entero = int(input('Ingrese un número entero: '))

    #sumatoria de numeros positivos
    if entero > 0:
        sumatoria_numeros_positivos += entero
        contador_positivos += 1

    #mayor numeros negativos
    else:
        if mayor_numeros_negativos == 0:
            mayor_numeros_negativos = entero
        if mayor_numeros_negativos < entero:
            mayor_numeros_negativos = entero

    #segundo menor
    if num == 0:
        menor = entero
    elif num == 1:
        if entero < menor:
            segundo_menor = menor
            menor = entero
        else:
            segundo_menor = entero
    else:
        if entero < menor:
            segundo_menor = menor
            menor = entero
        else:
            segundo_menor = entero



promedio_numeros_enteros_positivos = sumatoria_numeros_positivos / contador_positivos

print(f'El segundo más chico ingresado es: {segundo_menor}')
print(f'El mayor de los números negativos es: {mayor_numeros_negativos}')
print(f'El sumatorio de los números positivos es: {promedio_numeros_enteros_positivos}')

