import random

class Estudiante:
    def __init__(self, legajo, nombre, promedio):
        self.legajo = legajo
        self.nombre = nombre
        self.promedio = promedio


    def __str__(self):
        return (f'Legajo: {self.legajo: >7} \n'
                f'Nombre: {self.nombre: >9} \n'
                f'Promedio: {self.promedio: >5}')


def generar_matriz(cant_años, cant_estudiantes):
    filas = cant_años
    columnas = cant_estudiantes
    matriz = [[0] * columnas for i in range(filas)]
    return matriz


def popular_matriz(matriz):
    base_nombres = ['Rodrigo', 'Charly', 'Edgard', 'Mingo', 'Micho', 'Tito', 'Negro', 'Gordo', 'Cabezon']

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            legajo = random.randint(1,9999)
            nombre = random.choice(base_nombres)
            promedio = round(random.uniform(3.5,9.99),2)

            estudiante = Estudiante(legajo, nombre, promedio)
            matriz[i][j] = estudiante

    return matriz


def mostrar_matriz(matriz_populada):
    for i in range(len(matriz_populada)):
        print(f'Año {i + 1}: ')

        fila = matriz_populada[i]
        for j in range(len(fila)):
            estudiante = fila[j]
            print(f'------- Estudiante {j + 1}: ')
            print(estudiante)

        print("-" * 30)



def principal():
    cant_estudiantes = int(input('Ingrese la cant de estudiantes matriculados: '))
    cant_años = int(input('Ingrese la cant de años de formación del instituto: '))

    matriz_generada = generar_matriz(cant_años, cant_estudiantes)
    matriz_populada = popular_matriz(matriz_generada)
    mostrar_matriz(matriz_populada)



if __name__ == '__main__':
    principal()
