
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


def ordenar_por_nombres(nombres, edades, sueldos):
    longitud_arreglos = len(nombres)

    for i in range(longitud_arreglos - 1):
        for j in range(i + 1, longitud_arreglos):
            if nombres[i] > nombres[j]:
                nombres[i], nombres[j] = nombres[j], nombres[i]
                sueldos[i], sueldos[j] = sueldos[j], sueldos[i]
                edades[i],  edades[j]  = edades[j], edades[i]

    return nombres, edades, sueldos




def main():
    cant_usuarios = int(input('Ingrese la cant de usuarios a ingresar: '))
    usuarios_nombres, usuarios_edad, usuarios_sueldos = generador_usuarios(cant_usuarios)

    print(usuarios_nombres)
    print(usuarios_edad)
    print(usuarios_sueldos)

    usuarios_ordenados_por_nombre = ordenar_por_nombres(usuarios_nombres, usuarios_edad, usuarios_sueldos)

    print(usuarios_ordenados_por_nombre)


if __name__ == '__main__':
    main()

