class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f'Los puntos ingresados son:\n'
                f'x: {self.x} \n'
                f'y: {self.y}')


    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 'Primer Cuadrante'
        elif self.x < 0 and self.y > 0:
            return 'Segundo Cuadrante'
        elif self.x < 0 and self.y < 0:
            return 'Tercer Cuadrante'
        else:
            return 'Cuarto Cuadrante'



def principal():
    punto_1 = Punto(1.55, 2.45)
    punto_2 = Punto(5.89, 7.88)

    if punto_1.cuadrante() == punto_2.cuadrante():
        print(f'Se encuentran en el mismo cuadrante: {punto_1.cuadrante()}')

    else:
        print(f'No se encuentran en el mismo cuadrante \n'
              f'El punto 1 está en el: {punto_1.cuadrante()} \n'
              f'El punto 2 está en el: {punto_2.cuadrante()}')


if __name__ == '__main__':
    principal()
