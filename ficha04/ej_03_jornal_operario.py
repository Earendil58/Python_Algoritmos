def validador_jornada(mensaje):
    while True:
        mensaje_recibido = input(mensaje).strip()

        if not mensaje_recibido:
            print('Por favor, ingrese un dígito correspondiente a su jornada.')
            continue

        try:
            mensaje_a_numero = int(mensaje_recibido)

            if mensaje_a_numero != 1 and mensaje_a_numero != 2:
                print('Por favor, ingrese 1 o 2')
            else:
                return mensaje_a_numero

        except ValueError:
            print("Entrada inválida, por favor ingrese un número válido.")


def main():
    ingreso_jornada = validador_jornada('Por favor, ingrese su índice de jornada. Las opciones son [1-Diurno] o [2-Nocturno]: ')
    print(f"Has seleccionado la jornada {ingreso_jornada}")


if __name__ == '__main__':
    main()
