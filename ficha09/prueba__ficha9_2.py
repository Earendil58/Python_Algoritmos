
archivo = open('cosa.txt', 'rt')

cadena = archivo.read()

archivo.close()

print(f'Esta es una nueva cadena: {cadena}')
