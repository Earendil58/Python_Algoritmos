import pickle
import os

class Libro:
    def __init__(self, cod, nombre, autor):
        self.cod = cod
        self.nombre = nombre
        self.autor = autor

    def __str__(self):
        return (f'Código: {self.cod: >5} \n'
                f'Nombre: {self.nombre: >10} \n'
                f'Autor: {self.autor: >10}')


def principal():
    libro_1 = Libro(101, 'Maniac', 'Benjamin Labatut')
    libro_2 = Libro(102, 'Un verdor terrible', 'Benjamin Labatut')
    libro_3 = Libro(103, 'Ficciones', 'Jorge Luis Borges')

    archivo = open('libros.dat', 'wb')
    pickle.dump(libro_1, archivo)
    pickle.dump(libro_2, archivo)
    pickle.dump(libro_3, archivo)

    archivo.close()
    print('Se grabaron los libros')

    archivo = open('libros.dat', 'rb')
    libro_1 = pickle.load(archivo)
    libro_2 = pickle.load(archivo)
    libro_3 = pickle.load(archivo)

    print(f'Libro 1: {libro_1}')
    print(f'Libro 2: {libro_2}')
    print(f'Libro 3: {libro_3}')

    tamaño_archivo = os.path.getsize('libros.dat')

    print(f'El tamaño del archivo es: {tamaño_archivo}')



if __name__ == '__main__':
    principal()






