# Generar un programa que cargue un lote de números enteros y positivos y que a través de un menú de opciones le permita al usuario
#
# Obtener el promedio de los números comprendidos entre dos valores ingresados por el usuario
# Obtener el menor número impar del lote
# Imprimir todos los números múltiplos de un valor ingresado por el usuario separados por comas


def generador_lote(cant_numeros):
    lote = []
    if cant_numeros > 0:
        for i in range(cant_numeros):
            numero = int(input(f'Ingrese un número (entero y positivo) a agregar al lote {i + 1}: '))
            while numero < 0:
                numero = int(input(f'Ingrese un número (entero y positivo) a agregar al lote {i + 1}: '))
            lote.append(numero)
    else:
        print('Por favor ingrese un número mayor a 0')
    return lote

def promedio_entre_dos_valores(val1, val2, lote):
    lote_a_promediar = lote[val1 - 1: val2]
    print(lote_a_promediar)


def principal():
    cant_numeros = int(input('Ingrese la cant de números a cargar: '))
    lote = generador_lote(cant_numeros)
    print(f'Los números ingresados son: {lote}')
    print('Ingrese dos valores, para cortar el array y dar promedio de números comprendido en ellos: ')
    val1 = int(input('Ingrese el valor 1: '))
    val2 = int(input('Ingrese el valor 2: '))
    lote_a_promediar = promedio_entre_dos_valores(val1, val2, lote)


if __name__ == '__main__':
    principal()
