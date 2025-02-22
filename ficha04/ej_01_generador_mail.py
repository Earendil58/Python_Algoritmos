
def generador_mail(nombre, apellido, dominio):
    try:
        if nombre[0] == apellido[0]:
            mail = nombre + apellido + dominio
        else:
            mail = nombre[0] + apellido + dominio

        return mail

    except ValueError:
        print('Por favor, devuelva un dato válido')



def verificador_letras(cadena):
    while True:
        if isinstance(cadena, str):
            return cadena.strip().lower()
        else:
            print('Lo ingresado no es una respuesta válida')



def main():

    DOMINIO = '@frc.utn.edu.ar'

    ingreso_nombre = verificador_letras(input('Por favor, ingrese su nombre: '))
    ingreso_apellido = verificador_letras(input('Por favor, ingrese su apellido: '))

    mail_generado = generador_mail(ingreso_nombre, ingreso_apellido, DOMINIO)

    print(f'Su nueva casilla de mail es: {mail_generado}')


if __name__ == '__main__':
    main()

