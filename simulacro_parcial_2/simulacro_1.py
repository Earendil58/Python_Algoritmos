def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_impar(caracter):
    return int(caracter) % 2 != 0

def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'

def es_letra_minuscula(caracter):
    return 'a' <= caracter <= 'z'

def es_vocal(caracter):
    return caracter in 'aeiouAEIOUÁÉÍÓÚ'

def es_consonante(caracter):
    return es_letra(caracter) and not es_vocal(caracter)

def calcular_promedio(cant, total):
    promedio = 0
    if total > 0:
        promedio = cant // total
    return promedio


def principal():
    #INGRESO TEXTO
    abrir = open('texto.txt', 'rt')
    texto = abrir.read()
    abrir.close()



    #INGRESO VARIABLES DE CONTEO Y AUXILIARES
    contador_caracter = 0
    r1 = r2 = r3 = r4 = 0
    palabra_mas_larga = None
    anterior = ''
    cant_d = 0
    cantidad_palabras_contadas = cantidad_letras_contadas = 0
    cantidad_vocales = cantidad_consonantes = 0

    inicia_digito = inicia_vocal = tiene_b = tiene_m = tiene_a = solo_letras_minusculas = False

    #PROCESO EL TEXTO
    for caracter in texto:
        #CONSIDERAMOS SI ESTAMOS ADENTRO DE UNA PALABRA
        if caracter != ' ' and caracter != '.':
            contador_caracter += 1

            if es_digito(caracter):
                if es_impar(caracter) and contador_caracter == 1:
                    inicia_digito = True

            elif es_vocal(caracter):
                cantidad_vocales += 1
                if contador_caracter == 1:
                    inicia_vocal = True

                if caracter == 'a' or caracter == 'A':
                    tiene_a = True

                if anterior == 'd' or anterior == 'D':
                    cant_d += 1

            elif es_consonante(caracter):
                cantidad_consonantes += 1
                if caracter == 'b' or caracter == 'B':
                    tiene_b = True
                if caracter == 'm' or caracter == 'M':
                    tiene_m = True


            if contador_caracter == 2 and es_letra_minuscula(caracter):
                solo_letras_minusculas = True

            elif not es_letra_minuscula(caracter):
                solo_letras_minusculas = False


            anterior = caracter


        #CONSIDERAMOS SI ESTAMOS AFUERA DE UNA PALABRA

        else:
            #PUNTO 1 RESPUESTA
            if inicia_digito and solo_letras_minusculas:
                r1 += 1

            #PUNTO 2 RESPUESTA
            if inicia_vocal and tiene_b:
                if palabra_mas_larga is None:
                    palabra_mas_larga = contador_caracter
                elif contador_caracter > palabra_mas_larga:
                    palabra_mas_larga = contador_caracter

            #PUNTO 3 RESPUESTA
            if cantidad_consonantes > cantidad_vocales:
                if not tiene_a and not tiene_m:
                    cantidad_letras_contadas += contador_caracter
                    cantidad_palabras_contadas += 1

            #PUNTO 4 RESPUESTA
            if cant_d >= 2 and es_vocal(anterior):
                r4 += 1


            contador_caracter = cantidad_consonantes = cantidad_vocales = cant_d = 0
            inicia_digito = inicia_vocal = solo_letras_minusculas = tiene_m = tiene_a = tiene_b = False



    r2 = palabra_mas_larga
    r3 = calcular_promedio(cantidad_letras_contadas, cantidad_palabras_contadas)

    print('Primer resultado:', r1)
    print('Segundo resultado:', r2)
    print('Tercer resultado:', r3)
    print('Cuarto resultado:', r4)


if __name__ == '__main__':
    principal()


