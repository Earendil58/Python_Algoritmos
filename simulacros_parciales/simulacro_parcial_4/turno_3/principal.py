import random
import os.path
import pickle
import clase

def menu():
    print('Elige entre alguna de las siguiente opciones')
    print('1) Cargar Arreglo')
    print('2) Mostrar arreglo')
    print('3) Combinacion del stock disponible')
    print('4) Generar archivo binario')
    print('5) Mostrar archivo binario')
    print('6) Salir')

    opcion = int(input('Ingrese alguna de las opciones presentadas: '))
    while opcion < 1 or opcion > 6:
        print(f'Por favor eliga una opción válida, recién ingresó {opcion}')
        opcion = int(input('Ingrese alguna de las opciones presentadas: '))

    return opcion



def validador_num_no_negativo(num):
    while num < 1:
        num = int(input('Por favor ingrese un número positivo: '))
    return num


def add_in_order(arreglo, pantalon):
    izq, der = 0, len(arreglo) - 1
    posicion = len(arreglo)

    while izq <= der:
        punto_medio = (izq + der) // 2
        if pantalon.cod_producto == arreglo[punto_medio].cod_producto:
            posicion = punto_medio
            break

        else:
            if pantalon.cod_producto < arreglo[punto_medio].cod_producto:
                der = punto_medio - 1
            else:
                izq = punto_medio + 1

    if izq > der:
        posicion = izq

    arreglo[posicion:posicion] = [pantalon]



def opcion_1(cant_pantlones):
    arreglo = []

    array_nombre_modelos = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez']

    for i in range(cant_pantlones):
        cod_producto = random.randint(100, 1500)
        nombre_modelo = random.choice(array_nombre_modelos)
        largo_talle = random.randint(30,50)
        cintura_talle = random.randint(30,50)
        tipo_tela = random.randint(1,3)
        stock_disponible = random.randint(1,1500)

        pantalon = clase.Pantalon(cod_producto, nombre_modelo, largo_talle, cintura_talle, tipo_tela, stock_disponible)

        add_in_order(arreglo, pantalon)

    return arreglo


def opcion_2(arreglo):
    for pantalon in arreglo:
        print(pantalon)



def opcion_4(arreglo, fd, t):
    archivo = open(fd, 'wb')
    for i in range(len(arreglo)):
        if arreglo[i].tipo_tela == t and arreglo[i].stock_disponible > 0:
            pickle.dump(arreglo[i], archivo)

    archivo.close()


def opcion_5(fd):
    if not os.path.exists(fd):
        print('No existe el archivo')
        return

    else:
        acumulador_stock_pantalones = 0
        pantalones_relevados = 0
        tamaño_archivo = os.path.getsize(fd)
        archivo_a_retornar = open(fd, 'rb')
        while archivo_a_retornar.tell() < tamaño_archivo:
            r = pickle.load(archivo_a_retornar)
            pantalones_relevados += 1
            acumulador_stock_pantalones += r.stock_disponible
            print(r)

        archivo_a_retornar.close()

        if pantalones_relevados > 0:
            promedio_stock_pantalones = round(acumulador_stock_pantalones / pantalones_relevados, 2)

        print(f'El stock promedio de los pantalones guardados en el archivo es de: {promedio_stock_pantalones}')




def principal():
    opcion_elegida = -1
    arreglo = False
    fd = ''

    while opcion_elegida != 6:
        opcion_elegida = menu()

        if opcion_elegida == 1:
            cant_pantalones = validador_num_no_negativo(int(input('Ingrese la cant de pantalones: ')))
            arreglo = opcion_1(cant_pantalones)
            print('Arreglo cargado!')
            print()
            print()

        elif opcion_elegida == 2:
            if arreglo:
                opcion_2(arreglo)
            else:
                print('Por favor ingrese primero el arreglo')


        elif opcion_elegida == 4:
            if arreglo:
                fd = input('Ingrese un nombre para el archivo: ') + '.dat'
                t = -1
                while t < 1 or t > 3:
                    t = int(input('Ingrese un valor para la tela: '))
                opcion_4(arreglo, fd, t)
                print('Archivo generado!')
                print()
                print()
            else:
                print('Por favor, primero genere el arreglo')


        elif opcion_elegida == 5:
            opcion_5(fd)




if __name__ == '__main__':
    principal()
