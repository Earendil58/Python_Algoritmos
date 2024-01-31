palabra = input('Ingrese la palabra enmascarada: ')

#Enmascarar la palabra

enmascarada = 'x' * (len(palabra) - 2)
primera_letra = palabra[0]
ultima_letra = palabra[-1]

print('La palabra enmascarada es: {}'.format(primera_letra + enmascarada + ultima_letra))
