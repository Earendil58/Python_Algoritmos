
def generador_usuarios(cant_usuarios):
    nombres = []
    edades = []
    sueldos = []

    for usuario in range(cant_usuarios):
        nombre = input(f'Ingrese el nombre del usuario ({usuario + 1}): ')
        edad = int(input(f'Ingrese la edad del usuario ({usuario + 1}): '))
        sueldo = int(input(f'Ingrese el sueldo del usuario ({usuario + 1}): '))
        print('-' * 90)

        nombres.append(nombre)
        edades.append(edad)
        sueldos.append(sueldo)

    return nombres,edades, sueldos


def ordenar(nombres, edades,sueldos):
    



def main():
    cant_usuarios = int(input('Ingrese la cant de usuarios a ingresar: '))
    usuarios_nombres, usuarios_edad, usuarios_sueldos = generador_usuarios(cant_usuarios)

    print(usuarios_nombres)
    print(usuarios_edad)
    print(usuarios_sueldos)


if __name__ == '__main__':
    main()

