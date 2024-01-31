VOCALES= ('a','e','i','o','u')

palabra = input('ingrese una palabra: ')

cantidad_letras = len(palabra)

if palabra[-1] in VOCALES:
    print('La palabra tiene vocales')

else:
    print('La palabra no tiene vocales')
