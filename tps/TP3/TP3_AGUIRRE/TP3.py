import os.path
from envio import *

def cargar_desde_archivo(arreglo, tc, ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print(f'El archivo:  {ruta_archivo} no existe, verifique su archivo')
        return

    primera_linea = True
    abrir_archivo = open(ruta_archivo, 'rt')
    for linea in abrir_archivo:
        if primera_linea is True:
            if "SC" in linea:
                tc = 'SF'
                primera_linea = False

            else:
                codigo_postal = linea[0:9].strip().upper()
                direccion = linea[9:29].strip()
                tipo = int(linea[29])
                pago = int(linea[30])

                envio = Envio(codigo_postal, direccion, tipo, pago)
                arreglo.append(envio)




def opcion1(arreglo, tc, ruta_archivo):
    if len(arreglo) != 0:
        opcion = int(input(('Desea borrar los datos previos? ( 1: si/ 2: no): ')))
        if opcion == 1:
            arreglo = []
            tipo_control = cargar_desde_archivo(arreglo, tc, ruta_archivo)
            print('---- Carga terminada ----')
        else:
            print('Carga cancelada, los datos vigentes se mantienen')

    else:
        tc = cargar_desde_archivo(arreglo, tc, ruta_archivo)

    return arreglo, tc



def principal():
    ruta_archivo = 'envios-tp3.txt'
    tipo_control = 'HC' #CONTROL POR DEFECTO
    arreglo = []

    opcion = None

    while opcion != 10:
        print("Trabajo Practico 3")
        print("1. Cargar arreglo desde archivo de texto")
        print("2. Cargar arreglo desde teclado")
        print("3. Listado ordenado")
        print("4. Busqueda por direccion")
        print("5. Busqueda por codigo postal")
        print("6. Cantidad de envios con direccion válida")
        print("7. Importe final acumulado")
        print("8. Envio con mayor importe")
        print("9. Importe final promedio")
        print("10. Salir")

        opcion = int(input("Ingrese numero de opcion: "))

        if opcion == 1:





if __name__ == '__main__':
    principal()
