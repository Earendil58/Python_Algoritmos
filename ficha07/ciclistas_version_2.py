

competidores = int(input('Ingrese la cant de competidores: '))

nombres_competidores = []
tiempos_competidores = []
mejor_tiempo = None
nombre_ganador = None
anterior = None
tiempos_totales = 0

for competidor in range(competidores):



    nombre_competidor = input('Ingrese el nombre del competidor: ')
    tiempo_competidor = float(input('Ingrese el tiempo del competidor: '))

    tiempos_totales += tiempo_competidor


    nombres_competidores.append(nombre_competidor)
    tiempos_competidores.append(tiempo_competidor)

    if competidor == 0:
        anterior = tiempo_competidor
        mejor_tiempo = tiempo_competidor
        nombre_ganador = nombre_competidor

    elif tiempo_competidor < mejor_tiempo:
        mejor_tiempo = tiempo_competidor
        nombre_ganador = nombre_competidor

    anterior = tiempo_competidor


tiempo_promedio = round(tiempos_totales / competidores,2)


print(f'Los nombres de los competidores fueron: {nombres_competidores}')
print(f'Los tiempos de los competidores fueron: {tiempos_competidores}')
print(f'El mejor tiempo fue: {mejor_tiempo} y lo obtuvo: {nombre_ganador}')
print(f'El tiempo promedio de la carrera fue de: {tiempo_promedio}')
