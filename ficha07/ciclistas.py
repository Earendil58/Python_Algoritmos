competidores = int(input('Ingrese la cant de competidores: '))

nombre = ''
tiempo = 0
tiempo_record = int(input('Ingrese el tiempo record: '))
menor_tiempo = 0
menor_nombre = None
suma_tiempos = 0

for i in range(competidores):
    nombre = input('Ingrese el nombre del competidor: ')
    tiempo = int(input('Ingrese el tiempo del competidor: '))


    # Búsqueda del menor tiempo
    # Tenemos que garantizar que menor_tiempo empiece igual al primer valor
    if i == 0 or tiempo < menor_tiempo:
        menor_tiempo = tiempo
        menor_nombre = nombre

    #promedioo: acumulador / contador
    suma_tiempos += tiempo

promedio_tiempos = suma_tiempos / competidores

if menor_tiempo < tiempo_record:
    print(f'El nuevo record lo tiene: {menor_nombre}, con el tiempo de: {menor_tiempo}')
else:
    print(f'El record todavía lo tiene el tiempo de: {tiempo_record}')


print(f'El mejor tiempo de la carrera fue de: {menor_nombre}')
print(f'El promedio de los tiempos es: {promedio_tiempos}')



