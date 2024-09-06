from math import sqrt

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_origen(self):
        return sqrt(self.x ** 2 + self.y ** 2)



punto_1 = Punto(1.5,7.5)

print(f'Valor de x: {punto_1.x}')
print(f'Valor de y: {punto_1.y}')

print(f'La distancia al origen, desde el punto, es: {punto_1.dist_origen()}')

puntos = Punto(1.75, 2.88)

puntos.z1 = 1.55
puntos.z2 = 4.53




