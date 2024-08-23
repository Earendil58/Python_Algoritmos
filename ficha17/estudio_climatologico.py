

# def popular_Arrays(cant_elementos_a_registrar):
#
#     temperaturas = []
#     regiones = []
#     dias = []
#
#     for elemento in range(cant_elementos_a_registrar):
#         dia = int(input(f'Ingrese el día en el que se registró la temperatura: '))
#         temperatura = float(input(f'Ingrese la temperatura registrada ({elemento + 1}): '))
#         region = int(input(f'Ingrese la región en donde se registró la temperatura({elemento + 1}): '))
#
#         temperaturas.append(temperatura)
#         regiones.append(region)
#         dias.append(dia)
#
#     print(f'temperaturas: {temperaturas}')
#     print(f'dias: {dias}')
#     print(f'regiones: {regiones}')

def cargar_datos():
    n = int(input("Ingrese la cantidad de muestras a registrar: "))
    temperaturas = [0.0] * n
    regiones = [0] * n
    dias = [0] * n
    for i in range(n):
        dia = int(input("Ingrese día: "))
        region = int(input("Ingrese región: "))
        temperatura = float(input("Ingrese temperatura: "))
        dias[i] = dia
        regiones[i] = region
        temperaturas[i] = temperatura
    return dias, regiones, temperaturas

def menu():
    print('-' * 90)
    print('Ingrese algunas de las siguientes opciones: ')
    print('1) Determinar el promedio general de temperatura')
    print('2) Dada una región, mostrar las temperaturas de la misma, ordenadas por dia, de menor a mayor')
    print('3) Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado')
    print('4) Determinar la cantidad de muestras por region (20 contadores)')
    opcion_elegida = int(input('Ingresa la opción elegida: '))
    print('-' * 90)

    return opcion_elegida

def promedio_gral_temperaturas(temperaturas):
    longitud_array_temperaturas = len(temperaturas)
    acumulador_temperaturas = None

    for temperatura in temperaturas:
        if acumulador_temperaturas is None:
            acumulador_temperaturas = temperatura
        else:
            acumulador_temperaturas += temperatura

    promedio_temperaturas = round(acumulador_temperaturas / longitud_array_temperaturas, 2)

    return promedio_temperaturas



def principal():
    dias, regiones, temperaturas = cargar_datos()
    opcion_elegida = menu()

    if opcion_elegida == 1:
        promedios_de_temperaturas = promedio_gral_temperaturas(temperaturas)
        print(f'El promedio de las temperaturas registradas es: {promedios_de_temperaturas}')



if __name__ == '__main__':
    principal()


