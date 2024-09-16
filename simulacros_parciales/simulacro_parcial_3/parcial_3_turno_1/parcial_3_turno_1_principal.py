from parcial_3_turno_1_clase import *
import random

def popular_arreglo_manual(cant_empleos):
    arreglo_empleos = []
    for i in range(cant_empleos):
        id_empleo = int(input(f'Ingrese el ID del empleo {i + 1}: '))
        descripcion = input(f'Ingrese la descrición del empleo {i + 1}: ')
        tipo_empleo = int(input(f'Ingrese el valor numérico del tipo de empleo {i + 1}: '))
        while tipo_empleo < 0 or tipo_empleo > 39:
            tipo_empleo = int(input(f'Ingrese el valor numérico del tipo de empleo {i + 1}: '))
        sueldo = float(input(f'Ingrese el sueldo estipulado para el empleo {i + 1}: '))
        while sueldo <= 0:
            sueldo = float(input(f'Ingrese el sueldo estipulado para el empleo {i + 1}: '))

        empleo = Empleo(id_empleo, descripcion, tipo_empleo, sueldo)
        arreglo_empleos.append(empleo)

    return arreglo_empleos


def popular_arreglo_automatico(cant_empleos):
    arreglo_empleos = []
    empleos_disponibles = ['domador_hamsters', 'arqueologo', 'superhéroe', 'economista', 'actor', 'maquinista', 'físico']
    for i in range(cant_empleos):
        id_empleo = random.randint(1, 100)
        descripcion = random.choice(empleos_disponibles)
        tipo_empleo = random.randint(0,39)
        sueldo = random.randint(1000, 14506)

        empleo = Empleo(id_empleo, descripcion, tipo_empleo, sueldo)
        arreglo_empleos.append(empleo)

    return arreglo_empleos


def validador(numero):
    while numero <= 0:
        numero = int(input(f'Error, se pidió un valor mayor a {0}, cargue de nuevo: '))
    return numero


def mostrar(arreglo_empleos):
    for empleo in arreglo_empleos:
        print(empleo)

def opcion2(arreglo_empleos):
    longitud_arreglo = len(arreglo_empleos)
    for i in range(longitud_arreglo):
        for j in range(0, longitud_arreglo - i - 1):
            if arreglo_empleos[j].descripcion > arreglo_empleos[j + 1]. descripcion:
                arreglo_empleos[j], arreglo_empleos[j + 1] = arreglo_empleos[j + 1], arreglo_empleos[j]

    sueldos_totales_a_pagar = 0
    for i in arreglo_empleos:
        sueldos_totales_a_pagar += i.sueldo

    return arreglo_empleos, sueldos_totales_a_pagar


def opcion3(arreglo_empleos):
    conteo_tipos = [0] * 40

    for empleo in arreglo_empleos:
        conteo_tipos[empleo.tipo_empleo] += 1

    print(f'Este es el conteo_tipos: {conteo_tipos}')

    for tipo in range(40):
        cantidad = conteo_tipos[tipo]
        if cantidad > 0:
            print(f'Tipo: {tipo}: {cantidad} empleos')



def opcion4(tipo_empleo_buscado, arreglo_empleos):
    for empleo in arreglo_empleos:
        if tipo_empleo_buscado == empleo.tipo_empleo:
            print(f'El empleo buscado existe: {empleo.descripcion} \n'
                  f'El sueldo para dicho empleo, es de: ${empleo.sueldo}')




def menu():
    print('----- Ingrese alguna de las siguientes opciones -----')
    print('1) Cargar empleos disponibles ')
    print('2) Mostrar datos de empleos disponibles')
    print('3) Determinar la cantidad de empleos que hay en el arreglo por cada tipo de empleo posible ')
    print('4) Determinar si existe un empleo cuyo número de identificación sea igual num, siendo num un valor que se carga por teclado')
    print('5) Salir.')
    opcion = int(input('Ingrese la opción elegida: '))

    while opcion <= 0 or opcion > 5:
        print('Ingrese una opción válida. [del 1 al 5] ')
        opcion = int(input('Ingrese la opción elegida: '))

    return opcion



def principal():
    arreglo_empleos = []
    opcion_elegida = 0

    while opcion_elegida != 5:
        opcion_elegida = menu()

        if opcion_elegida == 1:
            cant_empleos = validador(int(input('Ingrese la cant de empleos: ')))
            arreglo_empleos = popular_arreglo_automatico(cant_empleos)
            print(f'Listo! El arreglo fue cargado.')
            print()
            print()


        elif opcion_elegida == 2:
            if arreglo_empleos:
                empleos_ordenados, sueldos_totales = opcion2(arreglo_empleos)
                mostrar(empleos_ordenados)
                print(f'El monto de los sueldos totales, a pagar, es de ${sueldos_totales}')
            else:
                print('El arreglo no fue cargado todavía, inicialice el arreglo con la opción 1.')

            print()
            print()


        elif opcion_elegida == 3:
            if arreglo_empleos:
                opcion3(arreglo_empleos)
            else:
                print('Por favor, primero cargue el arreglo')
            print()
            print()

        elif opcion_elegida == 4:
            if arreglo_empleos:
                tipo_empleo_buscado = int(input('Por favor, ingrese el tipo de empleo buscado (opciones válida del [0 al 39]) :'))
                while tipo_empleo_buscado < 0 or tipo_empleo_buscado > 39:
                    print('Por favor, ingrese una opción válida, las opciones van del 0 al 39 (incluidos)')
                    tipo_empleo_buscado = int(input('Por favor, ingrese el tipo de empleo buscado (opciones válida del [0 al 39]) :'))
                opcion4(tipo_empleo_buscado, arreglo_empleos)
            else:
                print('Por favor, primero cargue el arreglo.')

        elif opcion_elegida == 5:
            print('Saliendo del programa')

        else:
            print('Por favor ingrese una opción válida')
            print()
            print()



if __name__ == '__main__':
    principal()

