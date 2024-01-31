apellido = input('ingrese apellido del candidato: ')
nombre = input('Ingrese nombre del candidato: ')
cant_votos = int(input('Ingrese cantidad de votos: '))


#INICIALES DEL CANDIDATO

apellido_ini = apellido[0]
nombre_ini = nombre[0]

print('El candidato: {}.{}, obtuvo {}'.format(nombre_ini, apellido_ini, cant_votos*'x'))
