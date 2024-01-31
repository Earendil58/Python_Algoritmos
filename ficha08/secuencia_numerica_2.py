
n = int(input('Ingresar la cota derecha de la secuencia numerica: '))

while n < 0:
    n = int(input('Ingresar la cota derecha de la secuencia numerica: '))


numero_terminado_en_5 = 0
primer_numero_ingresado_por_usuario = None
primer_numero_ingresado_por_usuario_cantidad = 0
anterior = None
cant_mayores = 0

for i in range(n):
    numero = int(input('Ingrese un número: '))


    if numero % 10 == 5:
        numero_terminado_en_5 += 1

    if primer_numero_ingresado_por_usuario == None:
        primer_numero_ingresado_por_usuario = numero

    if numero == primer_numero_ingresado_por_usuario:
        primer_numero_ingresado_por_usuario_cantidad += 1

    if anterior == None:
        anterior = numero

    if numero > anterior:
        cant_mayores += 1

    anterior = numero


print(f'La cantidad de números que terminarn en 5 son: {numero_terminado_en_5}')
print(f'La cantidad de veces que apareció, el primer número ingresado por el usuario ({primer_numero_ingresado_por_usuario}), fue: {primer_numero_ingresado_por_usuario_cantidad}')
print(f'La cantidad de números ingresados, mayores que el anterior fue de: {cant_mayores}')



