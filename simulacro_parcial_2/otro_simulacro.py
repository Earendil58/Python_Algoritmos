#INGRESO MIS FUNCIONES

def es_digito(car):
    return '0' <= car <= '9'

def es_impar(car):
    return int(car) % 2 == 1

def es_letra(car):
    return 'a' <= car <= 'z' or 'A' <= car <= 'Z'

def es_minuscula(car):
    return 'a' <= car <= 'z'

def es_vocal(car):
    return car in 'aeiouAEIOUÁÉÍÓÚ'

def es_consonante(car):
    return es_letra(car) and not es_vocal(car)

def calcular_promedio(cant, total):
    promedio = 0
    if total > 0:
        promedio = cant // total
    return promedio



#INGRESO FUNCION PRINCIPAL
def principal():
    #PROCESO EL TEXTO
    cadena = open('nuevo-texto.txt', 'rt')
    texto = cadena.read()
    cadena.close()

    #INGRESO MIS VARIABLES AUXILIARES Y DE CONTEO
    contador_de_caracteres = 0
    r1 = r2 = r3 = r4 = 0
    cant_d = 0
    palabra_mas_larga = None
    cant_vocales = cant_consonantes = 0
    cantidad_letras_contadas = 0
    cantidad_palabras_contadas = 0
    anterior = ''

    #INGRESO MIS BANDERAS
    inicia_digito = inicia_vocal = tiene_b = tiene_m = tiene_a = solo_letras_minusculas = False


    #ITERO EL TEXTO
    for car in texto:
        #CONSIDERO QUE PASA SI ESTOY DENTRO DE UNA PALABRA
        if car != ' ' and car != '.':
            contador_de_caracteres += 1

            if es_digito(car):
                if es_impar(car) and contador_de_caracteres == 1:
                    inicia_digito = True

            elif es_vocal(car):
                cant_vocales += 1
                if anterior == 'd' or anterior == 'D':
                    cant_d += 1

            elif es_consonante(car):
                cant_consonantes += 1


            if contador_de_caracteres == 2 and es_minuscula(car):
                solo_letras_minusculas = True
            elif not es_minuscula(car):
                solo_letras_minusculas = False

            anterior = car

        #CONSIDERO QUE PASA SI ESTOY AFUERA DE UNA PALABRA
        else:

            if inicia_digito and solo_letras_minusculas:
                r1 += 1

            elif cant_d >= 2 and es_vocal(anterior):
                r4 += 1

            contador_de_caracteres = cant_d = cant_consonantes = cant_vocales = 0
            inicia_digito = inicia_vocal = solo_letras_minusculas =  tiene_b = tiene_m = tiene_a = False




    print("Primer resultado:", r1)
    print("Cuarto resultado:", r4)


#EJECUTO FUNCION PRINCIPAL
if __name__ == '__main__':
    principal()


