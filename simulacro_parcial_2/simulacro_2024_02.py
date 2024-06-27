def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'

def es_minuscula(caracter):
    return 'a' <= caracter <= 'z'

def es_vocal(caracter):
    return caracter in 'aeiouáéíóúAEIOUÁÉÍÓÚ'

def es_consonante(caracter):
    return es_letra(caracter) and not es_vocal(caracter)

def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_impar(caracter):
    return int(caracter) % 2 != 0



def principal():
    tratar_archivo = open('simulacro_2024_01.txt')
    texto = tratar_archivo.read()
    print(texto)
    tratar_archivo.close()


    # R1 FLAGS
    cant_de_letras_por_palabra = 0
    empieza_digito_impar = False
    tiene_letras_minusculas_dsp_del_digito = False
    cant_palabras_empiezan_digito_siguen_con_minusculas = 0

    # R2 FLAGS
    tiene_b = False
    empieza_vocal = False
    palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b = None

    for letra in texto:
        if letra == ' ' or letra == '.':

            if empieza_digito_impar and tiene_letras_minusculas_dsp_del_digito:
                cant_palabras_empiezan_digito_siguen_con_minusculas += 1

            if empieza_vocal and tiene_b:
                if palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b is None:
                    palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b = cant_de_letras_por_palabra
                elif cant_de_letras_por_palabra > palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b:
                    palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b = cant_de_letras_por_palabra


            # RESETEO FLAGS R1
            cant_de_letras_por_palabra = 0
            empieza_digito_impar = False
            tiene_letras_minusculas_dsp_del_digito = True

            #RESETEO FLAGS R2
            empieza_vocal = tiene_b = False




        else:
            cant_de_letras_por_palabra += 1

            if es_digito(letra):
                if cant_de_letras_por_palabra == 1 and es_impar(letra):
                    empieza_digito_impar = True

            elif es_consonante(letra):
                if letra == 'b' or letra == 'B':
                    tiene_b = True


            elif es_vocal(letra):
                if cant_de_letras_por_palabra == 1:
                    empieza_vocal = True


            if cant_de_letras_por_palabra == 2 and es_minuscula(letra):
                tiene_letras_minusculas_dsp_del_digito = True

            elif not es_minuscula(letra):
                tiene_letras_minusculas_dsp_del_digito = False


    r1 = cant_palabras_empiezan_digito_siguen_con_minusculas
    r2 = palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b


    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    # print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)



if __name__ == '__main__':
    principal()
