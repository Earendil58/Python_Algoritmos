import pickle
import os

class Libro:
    def __init__(self, cod, libro, autor):
        self.cod = cod
        self.libro = libro
        self.autor = autor

    def __str__(self):
        return (f'Código: {self.cod: <10} \n'
                f'Libro: {self.libro: <10} \n'
                f'Autor: {self.autor <10}')



def principal():
    libro_1 = Libro(101, '100 Años de soledad', 'Garcia Marquez')
    libro_2 = Libro(102, 'La Mente del niño', 'Maria Montessori')
    libro_3 = Libro(103, 'Ficciones', 'Jorge Luis Borges')

    archivo = open('libros.dat', 'wb')
    pickle.dump(libro_1, archivo)
    pickle.dump(libro_2, archivo)
    pickle.dump(libro_3, archivo)



