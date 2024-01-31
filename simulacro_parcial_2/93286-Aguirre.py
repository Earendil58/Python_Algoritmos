#DEFINO MIS FUNCIONES
def es_impar(car):
    return int(car) % 2 == 1

def es_digito(car):
    return '0' <= car <= '9'

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




#DEFINO MI FUNCION PRINCIPAL
def principal():
    #INGRESO EL TEXTO
    cadena = open('nuevo-texto.txt', 'rt')
    texto = cadena.read()
    cadena.close()

    #DECLARO VARIABLES AUXILIARES Y DE CONTEO
    conteo_caracter = 0
    r1 = r2 = r3 = r4 = 0
    cant_consonantes = cant_vocales = 0
    cantidad_letras_contadas = 0
    cantidad_palabras_contadas = 0
    cant_d = 0
    anterior = ''
    palabra_mas_larga = None

    #DECLARO BANDERAS
    inicia_digito = solo_letras_minusculas = inicia_vocal = tiene_b = tiene_m = tiene_a = False

    #PROCESO EL TEXTO
    for car in texto:

        #CONSIDERO SI ESTOY ADENTRO DE UNA PALABRA
        if car != ' ' and car != '.':
            conteo_caracter += 1

            if es_digito(car):
                if es_impar(car) and conteo_caracter == 1:
                    inicia_digito = True

            elif es_vocal(car):
                cant_vocales += 1
                if conteo_caracter == 1:
                    inicia_vocal = True
                if car == 'a' or car == 'A':
                    tiene_a = True
                if anterior == 'd' or anterior == 'D':
                    cant_d += 1



            elif es_consonante(car):
                cant_consonantes += 1
                if car == 'b' or car == 'B':
                    tiene_b = True
                if car == 'm' or car == 'M':
                    tiene_m = True


            if conteo_caracter == 2 and es_minuscula(car):
                solo_letras_minusculas = True
            elif not es_minuscula(car):
                solo_letras_minusculas = False

            anterior = car

        #CONSIDERO SI ESTOY AFUERA DE UNA PALABRA
        else:
            #PUNTO 1 RESPUESTA
            if inicia_digito and solo_letras_minusculas:
                r1 += 1

            #PUNTO 2 RESPUESTA
            if inicia_vocal and tiene_b:
                if palabra_mas_larga is None:
                    palabra_mas_larga = conteo_caracter
                elif conteo_caracter > palabra_mas_larga:
                    palabra_mas_larga = conteo_caracter

            #PUNTO 3 RESPUESTA
            if cant_consonantes > cant_vocales:
                if not tiene_a and not tiene_m:
                    cantidad_letras_contadas += conteo_caracter
                    cantidad_palabras_contadas += 1

            #PUNTO 4 RESPUESTA
            if cant_d >= 2 and es_vocal(anterior):
                r4 += 1



            conteo_caracter = cant_vocales = cant_consonantes = cant_d = 0
            inicia_digito = inicia_vocal = solo_letras_minusculas = tiene_b = tiene_m = tiene_a = False

    r2 = palabra_mas_larga
    r3 = calcular_promedio(cantidad_letras_contadas, cantidad_palabras_contadas)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print('Tercer resultado:', r3)
    print("Cuarto resultado:", r4)



#DEFINO LA FUNCION QUE EJECUTARÁ LA FUNC PRINC
if __name__ == '__main__':
    principal()
