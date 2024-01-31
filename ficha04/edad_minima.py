edad_minima = int(input('Ingrese la edad mínima: '))
edad_primer_persona = int(input('Ingrese su edad: '))
edad_segunda_persona = int(input('Ingrese su edad: '))
edad_tercer_persona = int(input('Ingrese su edad: '))

if edad_primer_persona >= edad_minima and edad_segunda_persona >= edad_minima and edad_tercer_persona >= edad_minima:
    print('Todos cumplen con le edad mínima requerida')
else:
    print('Al menos una persona no cumple con la edad mínima requerida')


print(f'Las edades ingresadas son: {edad_primer_persona}, {edad_segunda_persona}, {edad_tercer_persona} y la edad minima es: {edad_minima}')
