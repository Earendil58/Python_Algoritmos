def obtener_cadena_valida(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor and valor.isalpha():
            return valor
        print("Por favor, ingrese un valor válido (solo letras).")


def validador_numerico(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print('El número debe ser mayor a 0')
        except ValueError:
            print('Por favor, ingrese un número válido')


def main():
    nombre_candidato = obtener_cadena_valida('Por favor, ingrese el nombre del candidato: ')
    apellido_candidato = obtener_cadena_valida('Por favor, ingrese el apellido del candidato: ')
    cant_votos = validador_numerico('Por favor, ingrese la cantidad de votos obtenidos por el candidato: ')

    print(f'El cantidado: {nombre_candidato} {apellido_candidato}, sacó: {cant_votos} \n'
          f'Barra de votos: {"X" * cant_votos}')


if __name__ == '__main__':
    main()
