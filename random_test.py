
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
dominio = input('Ingrese su dominio: ')

if nombre[0] == apellido[0]:
    print(f'La direccion de mail es : {nombre}.{apellido}@{dominio}')
else:
    print(f'La direccion de mail es : {nombre[0]}.{apellido}@{dominio}')
