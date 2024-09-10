from parcial_3_turno_1_clase import *
import random

def popular_arreglo_manual(cant_empleos):
    arreglo_empleos = []
    for i in range(cant_empleos):
        id_empleo = int(input(f'Ingrese el ID del empleo {i + 1}: '))
        descripcion = input(f'Ingrese la descrición del empleo {i + 1}: ')
        tipo_empleo = int(input(f'Ingrese el valor numérico del tipo de empleo {i + 1}: '))
        sueldo = float(input(f'Ingrese el sueldo estipulado para el empleo {i + 1}: '))

        empleo = Empleo(id_empleo, descripcion, tipo_empleo, sueldo)
        arreglo_empleos.append(empleo)

    return arreglo_empleos


def popular_arreglo_automatico():
    arreglo_empleos = []
    empleos_disponibles = ['domador_hamsters', 'arqueologo', 'superhéroe', 'economista', 'actor', 'maquinista', 'físico']
    for i in range(empleos_disponibles):
        id_empleo = random.randint(1, 100)
        descripcion = random.choice(empleos_disponibles)
        tipo_empleo = random.randint(0,39)
        sueldo = random.randint(1000, 14506)

        empleo = Empleo(id_empleo, descripcion, tipo_empleo, sueldo)
        arreglo_empleos.append(empleo)

    return arreglo_empleos


def validador(inferior):
    n = int(input(f'Se necesita un valor mayor a {inferior} por favor: '))
    while n <= inferior:
        n = int(input(f'Error, se pidió un valor mayor a {inferior}, cargue de nuevo: '))
    return n

def mostrar(arreglo_empleos):
    for empleo in arreglo_empleos:
        print(empleo)




def principal():
    cant_empleos = validador(0)
    array_empleos = popular_arreglo_manual(cant_empleos)
    mostrar(array_empleos)



if __name__ == '__main__':
    principal()
