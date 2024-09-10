class Atleta:
    def __init__(self, nombre: str, tiempo_natacion: int, tiempo_ciclismo: int, tiempo_corriendo: int):
        self.nombre = nombre
        self.tiempo_natacion = tiempo_natacion
        self.tiempo_ciclismo = tiempo_ciclismo
        self.tiempo_corriendo = tiempo_corriendo


    def __str__(self):
        return (f"""El atleta y sus tiempos son:
                    nombre: {self.nombre}
                    tiempo en natacion: {self.tiempo_natacion}
                    tiempo en ciclismo: {self.tiempo_ciclismo}
                    tiempo en running:  {self.tiempo_corriendo}""")


    def tiempo_promedio(self):
        tiempo_promedio = round((self.tiempo_corriendo + self.tiempo_ciclismo + self.tiempo_natacion) / 3, 2)
        return tiempo_promedio


def popular_arreglo(cant_competidores):
    competidores = []
    for i in range(cant_competidores):
        nombre = input('Ingrese el nombre del competidor: ')
        tiempo_natacion = int(input('Ingrese el tiempo de natación: '))
        tiempo_ciclismo = int(input('Ingrese el tiempo de ciclismo: '))
        tiempo_corriendo = int(input('Ingrese el tiempo de running: '))

        competidor = Atleta(nombre, tiempo_natacion, tiempo_ciclismo, tiempo_corriendo)
        competidores.append(competidor)

    return competidores


def mostrar_competidores(competidores):
    for competidor in competidores:
        print(competidor)
        print(f'El tiempo promedio, para este competidor, fue de: {competidor.tiempo_promedio()} minutos')


def podio(arreglo_competidores):
    largo_arreglo = len(arreglo_competidores)
    for i in range(largo_arreglo):
        for j in range(0, largo_arreglo - i - 1):
            if arreglo_competidores[j].tiempo_promedio() > arreglo_competidores[j + 1].tiempo_promedio():
                arreglo_competidores[j], arreglo_competidores[j + 1] = arreglo_competidores[j + 1] , arreglo_competidores[j]

    return arreglo_competidores

def mostrar_podio(arreglo_competidores_podio):
    primeros_tres = arreglo_competidores_podio[0:3]
    primeros_tres_longitud = len(primeros_tres)
    for podio in range(primeros_tres_longitud):
        print(f'''El {podio + 1} de los competidores es: {primeros_tres[podio].nombre} 
                  Sus tiempos fueron: {primeros_tres[podio]}
                  El promedio de carrera fue: {primeros_tres[podio].tiempo_promedio()}''')



def test():
    cant_competidores = int(input('Ingrese la cant de competidores: '))
    arreglo_competidores = popular_arreglo(cant_competidores)
    # mostrar_competidores(arreglo_competidores)
    podio_competidores = podio(arreglo_competidores)
    # mostrar_competidores(podio_competidores)
    mostrar_podio(podio_competidores)


if __name__ == '__main__':
    test()

