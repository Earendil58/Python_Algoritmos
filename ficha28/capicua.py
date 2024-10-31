import stack


def capicua(cadena):
    longitud_cadena = len(cadena)
    pila = stack.Stack()

    mitad_cadena = longitud_cadena // 2
    if longitud_cadena % 2 == 1:
        d = mitad_cadena + 1
    else:
        d = mitad_cadena

    for i in range(mitad_cadena):
        pila.push(cadena[i])

    for i in range(d, longitud_cadena):
        x = pila.pop()
        if x != cadena[i]:
            return False
        return True



def main():
    cadena = input('Ingrese una cadena: ')
    res = capicua(cadena)
    if res:
        print('La cadena es capicúa...')
    else:
        print('La cadena no es capicúa...')

if __name__ == '__main__':
    main()
