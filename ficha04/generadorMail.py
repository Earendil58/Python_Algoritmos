print('#' * 30)
print('# ' + 'Generador de Mails' + \
 (' ' * (30-(len('Generador de Mails')+5))) + '#')
print('#' * 30)

nombre = input('ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
dominio = input('Ingrese su dominio: ')


if(nombre[0] == apellido[0]):
    print('{}.{}@{}'.format(nombre,apellido, dominio))

else:
    print('{}{}@{}'.format(nombre[0],apellido,dominio))
