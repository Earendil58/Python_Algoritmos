def generador_mail(nombre, apellido, dominio):

    if not nombre or not apellido:  # Evita nombres/apellidos vacíos
        return "Error: Nombre y apellido no pueden estar vacíos."

    if nombre[0].lower() == apellido[0].lower():
        mail = f"{nombre}.{apellido}{dominio}"
    else:
        mail = f"{nombre[0]}{apellido}{dominio}"

    return mail.lower()



def verificador_letras(mensaje):
    while True:
        cadena = input(mensaje).strip()
        if cadena.replace(" ", "").isalpha():
            return cadena.lower()
        else:
            print("Entrada inválida. Por favor, ingrese solo letras.")



def main():

    DOMINIO = '@frc.utn.edu.ar'

    ingreso_nombre = verificador_letras('Por favor, ingrese su nombre: ')
    ingreso_apellido = verificador_letras('Por favor, ingrese su apellido: ')

    mail_generado = generador_mail(ingreso_nombre, ingreso_apellido, DOMINIO)

    print(f'Su nueva casilla de mail es: {mail_generado}')


if __name__ == '__main__':
    main()

