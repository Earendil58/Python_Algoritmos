

mail = input('Ingrese su mail, con el formato nombre@dominio: ')
arroba = None
anterior = None
mail_longitud = len(mail)

for letra in mail:
    if mail[0] == '@' or mail[-1] == '@':
        print('Necesitas ingresar una dirección válida de mail')

    elif mail[0] == '.' or mail[-1] == '.':
        print('No podés empezar o terminar el mail con un ".", no es una dirección válida')


    if anterior == None:
        anterior = letra

    if letra == '.' and anterior == '.':
        print('No puede contener dos puntos seguidos')



    anterior = letra


print(f'Su mail ingresado es: {mail}')
