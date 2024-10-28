import random
import os.path
import pickle
import clase

def menu():
    print('Ingrese alguna de las siguientes opciones')
    print('1) Cargar arreglo')
    print('2) Mostrar arreglo')
    print('3) Buscar por vehículo ISBN')
    print('4) Generar archivo binario')
    print('5) Mostrar archivo binario')
    print('0) Salir')

    opcion = int(input('Ingrese algunas de las opciones mencionadas: '))
    while opcion < 0 or opcion > 5:
        print(f'Por favor, ingrese alguna opción entre 0 y 5. Usted ingresó: {opcion}')
        opcion = int(input('Ingrese algunas de las opciones mencionadas: '))

    return opcion


def validar_num_no_negativo(num):
    while num < 1:
        num = int(input('Por favor ingrese un número positivo: '))
    return num


def add_in_order(arreglo, libro):
    longitud_arreglo = len(arreglo)
    posicion = longitud_arreglo # si no hay otra mejor, pongo al final

    izq, der = 0, len(arreglo) - 1

    while izq <= der:
        punto_medio = (izq + der) // 2
        if libro.nro_isbn == arreglo[punto_medio].nro_isbn:
            posicion = arreglo[punto_medio]
            break

        else:
            if libro.nro_isbn < arreglo[punto_medio].nro_isbn:
                der = punto_medio - 1
            else:
                izq = punto_medio + 1

    if izq > der:
        posicion = izq

    arreglo[posicion:posicion] = [libro]



def opcion_1(cant_libros):
    arreglo = []

    combinacion_para_titulos = ['La guerra y la paz', 'Ficciones', 'El jardin de los senderos que se bifurcan', '100 años de soledad', 'titulo 1', 'titulo 2']
    combinacion_para_autores_nombre = ['Jorge', 'Luis', 'Sandra', 'Irma', 'Rodri']
    combinacion_para_autorires_apellidos = ['Menem', 'Cavallo', 'Ruckauf', 'Firmenich', 'Caputo']


    for i in range(cant_libros):
        numero_isbn = random.randint(10**12, 10**13 - 1)
        titulo = random.choice(combinacion_para_titulos)
        autor = f'{random.choice(combinacion_para_autores_nombre)} {random.choice(combinacion_para_autorires_apellidos)}'
        cod_idioma = random.randint(1,5)
        precio_venta = random.randint(10000,50000)

        libro = clase.Libro(numero_isbn, titulo, autor, cod_idioma, precio_venta)
        add_in_order(arreglo, libro)

    return arreglo



def opcion_2(arreglo):
    for libro in arreglo:
        print(libro)


def opcion_4(arreglo, fd, a, p):
    longitud_arreglo = len(arreglo)
    archivo = open(fd, 'wb')

    for i in range(longitud_arreglo):
        if arreglo[i].autor == a and arreglo[i].precio_venta <= p:
            pickle.dump(arreglo[i], archivo)

    archivo.close()

    print('Archivo generado!')


def opcion_5(fd):
    if not os.path.exists(fd):
        print('Lo lamento, el archivo no existe')
        print()
        return

    else:
        cantidad_libro_a_mostrar = 0
        archivo_a_trabajar = open(fd, 'rb')
        tamaño_archivo = os.path.getsize(fd)
        while archivo_a_trabajar.tell() < tamaño_archivo:
            r = pickle.load(archivo_a_trabajar)
            cantidad_libro_a_mostrar += 1
            print(r)
        archivo_a_trabajar.close()

        print(f'La cantidad de libros mostrados es: {cantidad_libro_a_mostrar}')





def principal():
    opcion_elegida = -1
    fd = None
    arreglo_cargado = False

    while opcion_elegida != 0:
        opcion_elegida = menu()

        if opcion_elegida == 1:
            cant_libros = validar_num_no_negativo(int(input('Ingrese la cant de libros: ')))
            arreglo_cargado = opcion_1(cant_libros)
            print('Arreglo cargado!')
            print()
            print()

        elif opcion_elegida == 2:
            if arreglo_cargado:
                opcion_2(arreglo_cargado)
                print()
                print()

            else:
                print('Por favor cargue primero el arreglo')
                print()
                print()

        elif opcion_elegida == 4:
            fd = input('Ingrese un nombre para el archivo a generar: ') + ".dat"
            a = input('Ingrese el nombre del autor a registrar: ')
            p = int(input('Ingrese el precio máximo a registrar: '))

            opcion_4(arreglo_cargado, fd, a, p)
            print()
            print()

        elif opcion_elegida == 5:
            opcion_5(fd)





if __name__ == '__main__':
    principal()
