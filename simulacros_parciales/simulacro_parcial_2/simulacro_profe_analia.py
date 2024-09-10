def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'

def es_vocal(caracter):
    return caracter in 'aeiouAEIOUÁÉÍÓÚ'

def consonante(caracter):
    return es_letra(caracter) and not es_vocal(caracter)

def es_digito(caracter):
    return '0' <= caracter <= '9'


def principal():
    print('Segundo Parcial')

    #1- INGRESAR EL TEXTO
    texto = input('Ingresar el texto (se termina con un .): ')

    #2- DEFINIR VARIABLES DE RESULTADO Y AUXILIARES
    car_anterior = ''
    cant_letras = 0
    cant_palabras = 0

    #3- PROCESAR EL TEXTO
    for caracter in texto:
        # CONSIDERAMOS SI ESTAMOS DENTRO DE UNA PALABRA
        if caracter != ' ' and caracter != '.':
            pass



        # CONSIDERAMOS SI ESTAMOS FUERA DE UNA PALABRA
        else:
            cant_palabras += 1
