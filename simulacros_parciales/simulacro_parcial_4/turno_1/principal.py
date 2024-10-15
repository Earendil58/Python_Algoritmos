import random
import pickle
import os
import clase


def menu():
    print('Ingrese alguna de las siguientes opciones: ')
    print('1) Cargar datos')
    print('2) Mostrar datos')
    print('3) Superficie total vendida por cada manzana posible combinada con cada orientación posible y a superficie total vendida para una manzana m')
    print('4) Generación de archivo binario de los lotes comprendidos entre L1 y L2 (Ingresados por teclado)')
    print('5) Mostrar el contenido de archivo binario y mostrar valor promedio de la venta de los lotes contenidos en el archivo')
    print('6) Salir')

    opcion = int(input('Ingrese la opción elegida: '))

    while opcion < 1 or opcion > 5:
        print(f'Por favor ingrese una opción válida, su opción elegida fue: {opcion}. El rango disponible es de 1 a 5')
        opcion = int(input('Ingrese la opción elegida: '))

    return opcion


def validador_carga_no_negativos(num):
    while num < 1:
        print(f'Por favor ingresa números positivos, el que ingresaste fue: {num}')
        num = int(input('Ingresa un número positivo: '))

    return num


def add_in_order(lote):
    pass



def opcion_1(cant_lotes):

    arreglo = [0] * cant_lotes

    nombres = ["Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad"]
    apellidos = ["Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte"]

    for i in range(cant_lotes):
        nombre = random.choice(nombres) + ' ' + random.choice(apellidos)
        nro_mza = random.randint(1,35)
        nro_lote = random.randint(1,20)
        orientacion = random.randint(1,4)
        superficie = round(random.uniform(200,4000),2)
        monto = round(random.uniform(10000,150000),2)

        lote = Lote(nombre, nro_mza,nro_lote,orientacion,superficie,monto)

        add_in_order(lote)



def principal():
    opcion_elegida = -1

    while opcion_elegida != 6:
        opcion_elegida = menu()

        if opcion_elegida == 1:
            cant_lotes = validador_carga_no_negativos(int(input('Ingresa la cantidad de lotes a cargar: ')))







if __name__ == '__name__':
    principal()
