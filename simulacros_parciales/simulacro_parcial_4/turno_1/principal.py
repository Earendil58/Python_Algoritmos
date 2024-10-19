import random
import pickle
import os.path
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


def add_in_order(arreglo, lote):
    izq, der = 0, len(arreglo) - 1
    posicion = len(arreglo)  # Por defecto, insertar al final si no se encuentra un lugar mejor

    # Búsqueda binaria para encontrar la posición de inserción
    while izq <= der:
        punto_medio = (izq + der) // 2
        if lote.nombre_completo < arreglo[punto_medio].nombre_completo:
            der = punto_medio - 1
            posicion = punto_medio  # Actualiza la posición donde se insertaría el lote
        else:
            izq = punto_medio + 1

    # Inserta el lote en la posición correcta
    arreglo[posicion:posicion] = [lote]



def opcion_1(cant_lotes):
    arreglo = []

    nombres = ["Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad"]
    apellidos = ["Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte"]

    for i in range(cant_lotes):
        nombre = random.choice(nombres) + ' ' + random.choice(apellidos)
        nro_mza = random.randint(1,35)
        nro_lote = random.randint(1,20)
        orientacion = random.randint(1,4)
        superficie = round(random.uniform(200,4000),2)
        monto = round(random.uniform(10000,150000),2)

        lote = clase.Lote(nombre, nro_mza,nro_lote,orientacion,superficie,monto)

        add_in_order(arreglo,lote)

    return arreglo



def opcion_2(arreglo):
    for lote in arreglo:
        print(lote)


def opcion_4(arreglo,fd, l1, l2):
    longitud_arreglo = len(arreglo)

    archivo = open(fd, 'wb')

    for i in range(longitud_arreglo):
        if l1 <= arreglo[i].nro_lote <= l2:
            pickle.dump(arreglo[i], archivo)

    archivo.close()
    print('Archivo generado')


def opcion_5(fd):
    if not os.path.exists(fd):
        print(f'El archivo {fd} no existe')
        print()
        print()
        return

    else:
        acumulador_ventas_lotes = 0
        cantilidad_lotes = 0
        tamaño_archivo = os.path.getsize(fd)
        archivo_a_trabajar = open(fd, 'rb')

        while archivo_a_trabajar.tell() < tamaño_archivo:
            r = pickle.load(archivo_a_trabajar)
            cantilidad_lotes += 1
            acumulador_ventas_lotes += r.monto_venta
            print(r)
        archivo_a_trabajar.close()

    promedio = 0

    if cantilidad_lotes != 0:
        promedio = round(acumulador_ventas_lotes / cantilidad_lotes, 2)

    print(f'Importe promedio de ventas: {promedio}')
    print()
    print()




def principal():
    opcion_elegida = -1
    arreglo_cargado = False
    fd = None

    while opcion_elegida != 6:
        opcion_elegida = menu()

        if opcion_elegida == 1:
            cant_lotes = validador_carga_no_negativos(int(input('Ingresa la cantidad de lotes a cargar: ')))
            arreglo_cargado = opcion_1(cant_lotes)
            print('Arreglo cargado!')
            print()
            print()

        elif opcion_elegida == 2:
            if arreglo_cargado:
                opcion_2(arreglo_cargado)
                print()
                print()
            else:
                print('Por favor, cargue el arreglo primero')
                print()
                print()

        elif opcion_elegida == 4:
            if arreglo_cargado:
                fd = input('Ingrese una descripción para el archivo: ') + ".dat"
                l1 = int(input("Valor de l1: "))
                l2 = int(input("Valor de l2: "))
                opcion_4(arreglo_cargado, fd, l1, l2)
                print()
                print()

            else:
                print('Por favor cargue el arreglo primero.')
                print()
                print()


        elif opcion_elegida == 5:
            if arreglo_cargado:
                opcion_5(fd)




if __name__ == '__main__':
    principal()
