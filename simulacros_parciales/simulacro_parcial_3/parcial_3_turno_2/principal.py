import random
from clase_empleo import *


def carga_automatica(cant_tickets):
    arreglo_tickets = []
    codigos_vuelos_disponibles = ['AB12', 'BA21', 'CD12', 'DC21', 'EF12','FE21', 'GH12', 'HG21', 'IJ12', 'JI21']
    precios_disponibles = [14526, 18452, 78451, 25412, 11245, 12365, 12547, 13652]

    for ticket in range(cant_tickets):
        cod_vuelo = random.choice(codigos_vuelos_disponibles)
        id_pasajero = random.randint(1,100)
        id_pais_destino = random.randint(1000,2000)
        numero_asiento = random.randint(1,50)
        importe_ticket = random.choice(precios_disponibles)

        ticket = Ticket(cod_vuelo, id_pasajero, id_pais_destino, numero_asiento, importe_ticket)
        arreglo_tickets.append(ticket)

    return arreglo_tickets

def opcion2(arreglo_tickets):
    for ticket in arreglo_tickets:
        print(ticket)




def menu():
    print(' ---------- Por favor, elija alguna de las siguientes opciones  ---------- ')
    print('1) Cargar los tickets')
    print('2) Mostrar los tickets')

    print('5) Salir')

    opcion = int(input('Por favor ingrese una de las opciones descriptas: '))
    while opcion < 1 or opcion > 5:
        print('Por favor ingrese una opción válida [del 1 al 5]')
        opcion = int(input('Por favor ingrese una de las opciones descriptas: '))

    return opcion



def principal():
    opcion_elegida = 0

    while opcion_elegida != 5:
        opcion_elegida = menu()

        if opcion_elegida == 1:
            cant_tickets = int(input('Ingrese la cantidad de tickets disponibles: '))
            while cant_tickets <= 0:
                print('Ingrese una cant positiva de tickets')
                cant_tickets = int(input('Ingrese la cantidad de tickets disponibles: '))
            arreglo_tickets = carga_automatica(cant_tickets)
            print('Carga lista!')
            print()
            print()

        elif opcion_elegida == 2:
            if arreglo_tickets:
                opcion2(arreglo_tickets)
            else:
                print('Por favor primero cargue el arreglo, vaya a la opción 1')

        elif opcion_elegida == 5:
            print('Nos re vimos, gato')




if __name__ == '__main__':
    principal()
