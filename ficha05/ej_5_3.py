from random import randint
from typing import Literal


Tipo_problema = Literal['software', 'hardware']
VALIDOS = {'software', 'hardware'}

tiempo_total_mantenimiento = 0
id_pc_mayor_mantenimiento = None
tiempo_promedio_tareas_mantenimiento = 0

for equipo in range(1, 4):
    id_pc = randint(1,2500)
    tiempo_reparacion_minutos = int(input('Tiempo de reparacion? : '))
    while True:
        problema_mantenimiento : Tipo_problema = (input('Problema (software/hardware)?').strip().lower())
        if problema_mantenimiento in VALIDOS:
            break
        print("Tipo inválido, intenta otra vez (software/hardware)")

    tiempo_total_mantenimiento += tiempo_reparacion_minutos

    if id_pc_mayor_mantenimiento is None:
        id_pc_mayor_mantenimiento = id_pc

    if id_pc > id_pc_mayor_mantenimiento:
        id_pc_mayor_mantenimiento = id_pc


tiempo_promedio_tareas_mantenimiento = round(tiempo_total_mantenimiento // 3, 2)

print(f'El tiempo promedio de las tareas de mantenimiento es: {tiempo_promedio_tareas_mantenimiento} min')
print(f'El ID de la PC con mayor tiempo de mantenimiento fue: {id_pc_mayor_mantenimiento}')
print(f'El tiempo total de las tareas de manteniento fue de: {tiempo_total_mantenimiento}')


