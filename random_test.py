

palabra_a_enmascarar = input('Ingrese la palabra: ')
palabra_enmascarada = ''
longitud_palabra = len(palabra_a_enmascarar)
contador = 0

for letra in palabra_a_enmascarar:
    contador += 1
    if contador == 1 or contador == longitud_palabra:
        palabra_enmascarada += letra
    else:
        palabra_enmascarada += '*'





print(f'La palabra enmascarada es: {palabra_enmascarada}')
