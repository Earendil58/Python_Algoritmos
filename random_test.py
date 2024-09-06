class Estudiante:
    def __init__(self, nombre, apellido, edad, carrera, año):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera
        self.año = año

    def __str__(self):
        return (f'Nombre: {self.nombre} \n'
                f'Apellido: {self.apellido} \n'
                f'Edad: {self.edad} \n'
                f'Carrera: {self.carrera} \n'
                f'Año: {self.año}')



def vector_estudiantes(cant_estudiantes):
    vector_estudiantes = []

    for i in range(cant_estudiantes):
        nombre = input('Ingrese el nombre del estudiante: ')
        apellido = input('Ingrese el apellido del estudiante: ')
        edad = int(input('Ingrese la edad del estudiante: '))
        carrera = input('Ingrese la carrera del estudiante: ')
        año = int(input('Ingrese el año del estudiante: '))

        estudiante = Estudiante(nombre, apellido, edad, carrera, año)

        vector_estudiantes.append(estudiante)

    return vector_estudiantes

def mostrar_estudiantes(vector_estudiantes):
    for estudiante in vector_estudiantes:
        print('Los estudiantes registrados son: ')
        print('-' * 90)
        print(estudiante)





def main():
    cant_estudiantes = int(input('Ingrese la cant de estudiantes: '))
    estudiantes = vector_estudiantes(cant_estudiantes)
    mostrar_estudiantes_registrados = mostrar_estudiantes(estudiantes)


if __name__ == '__main__':
    main()
