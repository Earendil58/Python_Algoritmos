class Estudiante:

    def __init__(self, nombre, apellido, legajo, promedio):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.promedio = promedio


    def __str__(self):
        return (f'Nombre: {self.nombre} \n'
                f'Apellido: {self.apellido} \n'
                f'Legajo: {self.legajo} \n'
                f'Promedio: {self.promedio}')


def vector_estudiantes(cant_estudiantes):
    estudiantes = []

    for i in range(cant_estudiantes):
        nombre = input('Ingrese el nombre del estudiante: ')
        apellido = input('Ingrese el apellido del estudiante: ')
        legajo = int(input('Ingrese el legajo del estudiante: '))
        promedio = float(input('Ingrese el promedio del estudiante: '))

        estudiante = Estudiante(nombre, apellido, legajo, promedio)
        estudiantes.append(estudiante)

    return estudiantes


def mostrar_estudiantes(estudiantes):
    print('Estos son los estudiantes:')
    for estudiante in estudiantes:
        print('-' * 90)
        print(estudiante)


def estudiantes_habilitados(estudiantes, promedio_necesario):
    estudiantes_participantes_habilitados = []

    for estudiante in estudiantes:
        if estudiante.promedio >= promedio_necesario:
            estudiantes_participantes_habilitados.append(estudiante)

    return estudiantes_participantes_habilitados


def orden_legajos_participantes(estudiantes_participantes_habilitados):
    longitud_arreglo = len(estudiantes_participantes_habilitados)

    for i in range(longitud_arreglo):
        for j in range(i + 1, longitud_arreglo - i - 1):
            if estudiantes_participantes_habilitados[i].legajo > estudiantes_participantes_habilitados[j].legajo:
                estudiantes_participantes_habilitados[i], estudiantes_participantes_habilitados[j] = estudiantes_participantes_habilitados[j], estudiantes_participantes_habilitados[i]

    return estudiantes_participantes_habilitados




def main():
    cant_estudiantes = int(input('Ingrese la cantidad de estudiantes anotados a participar del concurso: '))
    vector_estudiantes_registrados = vector_estudiantes(cant_estudiantes)
    mostrar_est = mostrar_estudiantes(vector_estudiantes_registrados)

    promedio_necesario_para_competir = float(input('Ingrese el promedio necesario para competir: '))
    est_habilitados = estudiantes_habilitados(vector_estudiantes_registrados, promedio_necesario_para_competir)
    mostrar_est_habilitados = mostrar_estudiantes(est_habilitados)

    est_habilitados_ordenados_por_legajo = orden_legajos_participantes(est_habilitados)
    mostrar_est_habilitados_ordenados_por_legajo = mostrar_estudiantes(est_habilitados_ordenados_por_legajo)


if __name__ == '__main__':
    main()

