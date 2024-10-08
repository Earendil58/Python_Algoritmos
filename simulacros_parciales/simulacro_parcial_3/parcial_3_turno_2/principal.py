import random
from clase_ticket import *


def carga_automatica(cant_tickets):
    arreglo_tickets = []
    codigos_vuelos_disponibles = ['AB12', 'BA21', 'CD12', 'DC21', 'EF12','FE21', 'GH12', 'HG21', 'IJ12', 'JI21']
    precios_disponibles = [14526, 18452, 78451, 25412, 11245, 12365, 12547, 13652]

    for ticket in range(cant_tickets):
        cod_vuelo = random.choice(codigos_vuelos_disponibles)
        id_pasajero = random.randint(1,100)
        id_pais_destino = random.randint(1,20)
        numero_asiento = random.randint(1,50)
        importe_ticket = random.choice(precios_disponibles)

        ticket = Ticket(cod_vuelo, id_pasajero, id_pais_destino, numero_asiento, importe_ticket)
        arreglo_tickets.append(ticket)

    return arreglo_tickets

def opcion2(arreglo_tickets, asiento_cota_inferior):
    arreglo_tickets_asientos_mayores_cota_inferior = []

    for ticket in arreglo_tickets:
        if ticket.num_asiento > asiento_cota_inferior:
            arreglo_tickets_asientos_mayores_cota_inferior.append(ticket)

    print(f'Este es el arreglo con cota inferior de asiento: {arreglo_tickets_asientos_mayores_cota_inferior}')

    longitud_arreglo = len(arreglo_tickets_asientos_mayores_cota_inferior)
    for i in range(longitud_arreglo):
        for j in range(0, longitud_arreglo - i - 1):
            if arreglo_tickets_asientos_mayores_cota_inferior[j].cod_vuelo > arreglo_tickets_asientos_mayores_cota_inferior[j + 1].cod_vuelo:
                arreglo_tickets_asientos_mayores_cota_inferior[j], arreglo_tickets_asientos_mayores_cota_inferior[j + 1] = arreglo_tickets_asientos_mayores_cota_inferior[j + 1], arreglo_tickets_asientos_mayores_cota_inferior[j]

    return arreglo_tickets_asientos_mayores_cota_inferior


def opcion3(arreglo_tickets, t):
    arreglo_con_id_paises_destino = [0] * 20


    # for i in range(len(arreglo_con_id_paises_destino)):
    #     indices_ajustados = arreglo_tickets[i].id_pais_destino - 1 #EL TRUCO ACÁ ERA AJUSTAR EL
    #     arreglo_con_id_paises_destino[indices_ajustados] += arreglo_tickets[i].importe_ticket

    for ticket in arreglo_tickets:
        arreglo_con_id_paises_destino[(ticket.id_pais_destino) - 1] += ticket.importe_ticket

    # for k in range(len(arreglo_con_id_paises_destino)):
    #     if arreglo_con_id_paises_destino[k] > t:
    #         print(f'Pais destino: {k + 1: <10}, importe acumulado: ${arreglo_con_id_paises_destino[k]: <10}')

    for k in range(len(arreglo_con_id_paises_destino)):
        if arreglo_con_id_paises_destino[k] > t:
            print(f'Pais destino: {k + 1: <10}, importe acumulado: ${arreglo_con_id_paises_destino[k]: <10}')


def opcion4(arreglo_tickets, id_pasajero):
    arreglo_id_pasajeros = [ticket.id_pasajero for ticket in arreglo_tickets]
    for ticket in arreglo_tickets:
        if ticket.id_pasajero == id_pasajero:
            print(f'El pasajero ID: {id_pasajero} fue encontrado \n' 
                  f'El ID de destino al que se dirige es: {ticket.id_pais_destino}')
            break
    if id_pasajero not in arreglo_id_pasajeros:
        print(f'El ID buscado: {id_pasajero} no se encuentra dentro de los pasajeros registrados')


def mostrar(arreglo):
    for ticket in arreglo:
        print(ticket)



def menu():
    print(' ---------- Por favor, elija alguna de las siguientes opciones  ---------- ')
    print('1) Cargar los tickets')
    print('2) Mostrar los tickets')
    print('3) Determine el importe acumulado que se cobró por cada posible país de destino')
    print('4) Determinar si existe un ticket cuyo número de identificación del pasajero sea igual a id.')

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
                asiento_cota_inferior = int(input('Número de asiento (se mostrarán los tickets cuyo número de asiento sea mayor a este): '))
                arreglo_ordenador_asientos_cod_vuelos = opcion2(arreglo_tickets, asiento_cota_inferior)
                mostrar(arreglo_ordenador_asientos_cod_vuelos)
                print()
                print()
            else:
                print('Por favor primero cargue el arreglo, vaya a la opción 1')

        elif opcion_elegida == 3:
            if arreglo_tickets:
                t = int(input('Ingrese la cota t: '))
                opcion3(arreglo_tickets, t)


        elif opcion_elegida == 4:
            if arreglo_tickets:
                id_pasajero_buscado = int(input('Ingrese el ID del pasajero a buscar: '))
                while id_pasajero_buscado < 1:
                    id_pasajero_buscado = int(input('Ingrese el ID del pasajero a buscar: '))
                opcion4(arreglo_tickets, id_pasajero_buscado)
                print()
                print()
            else:
                print('Por favor, ingrese el arreglo primero')


        elif opcion_elegida == 5:
            print('Nos re vimos, gato')




if __name__ == '__main__':
    principal()
