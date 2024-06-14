def tipo_control(texto):
    texto_normalizado = texto.lower().strip()

    anterior = ''
    time_stamp = ''

    for letra in texto_normalizado:
        if letra != '\n':
            time_stamp += letra

        else:
            break

    for letra in time_stamp:
        if anterior == 'h' and letra == 'c':
           return 'Hard Control'

        if anterior == 's' and letra == 'c':
            return 'Soft Control'

        anterior = letra



def procesar_oracion(texto):
    oracion = ''
    indice = 0
    longitud_texto = len(texto)

    while indice < longitud_texto:
        caracter = texto[indice]

        if caracter == '\n':
            if oracion:
                print(oracion.strip())
                oracion = ''
        else:
            oracion += caracter

        indice += 1

    if oracion:
        print(oracion)


def hard_control(oracion):

    texto_normalizado = oracion.lower()

    caracter_especial = False
    tuvo_mayuscula = False
    mayusculas_consecutivas = False
    palabra_compuesta_solo_digitos = False

    for letra in texto_normalizado:
        if 'A' >= letra >= 'Z' or 'a' >= letra >= 'z':
            caracter_especial = True

        if letra 




def leer_archivo():
    manejar_archivo = open('envios25.txt', 'rt')
    texto = manejar_archivo.read()
    manejar_archivo.close()
    return texto


def main():
    texto = leer_archivo()

    tipo_de_control = tipo_control(texto)

    print(tipo_de_control)


main()



