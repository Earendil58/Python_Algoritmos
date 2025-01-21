def validador_numerico():
    while True:
        try:
            importe = float(input('Por favor, ingrese un importe válido: '))
            if importe > 0:
                return importe
            else:
                print('Por favor, ingrese un importe positivo')
        except ValueError:
            print('Entrada no válida. Por favor, ingrese un número')



def main():
    importe = validador_numerico()

    print(f'El importe ingresado es:  ${importe: .2f}')
    print(f'El importe ingresado es: pesos {importe: .2f}')


if __name__=='__main__':
    main()
