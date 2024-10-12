import os
import pickle

def test():
    archivo = open('coso.txt', 'wb')

    x = 'Hola, soy una oración'
    y = 14578454554.545115
    pickle.dump(x, archivo)
    pickle.dump(y, archivo)

    archivo.close()

    archivo = open('coso.txt', 'rb')
    a = pickle.load(archivo)
    b = pickle.load(archivo)

    archivo.close()

    print(f'Archivos recuperados: {a} y {b}')


if __name__ == '__main__':
    test()


