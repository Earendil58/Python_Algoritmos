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

def promedio_entero(cantidad, totales):
    promedio = 0
    if totales > 0:
        promedio = cantidad // totales
    return promedio



def principal():
    tratar_archivo = open('simulacro_2024_01.txt')
    texto = tratar_archivo.read()
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

    # R3 FLAGS
    cant_letras_totales_en_texto = 0
    cant_consonantes = 0
    cant_vocales = 0
    tiene_a = False
    tiene_m = False
    cant_palabras_que_tienen_mas_consonantes_que_vocales_y_no_tienen_a_o_m = 0
    cant_letras_de_palabras_que_tienen_mas_consonantes_que_vocales_y_no_tienen_a_o_m = 0

    # R4 FLAGS
    cant_d = 0
    cant_palabras_incluyen_dos_o_mas_veces_d_y_vocal_y_terminan_en_vocal = 0

    for letra in texto:
        if letra == ' ' or letra == '.':

            if empieza_digito_impar and tiene_letras_minusculas_dsp_del_digito:
                cant_palabras_empiezan_digito_siguen_con_minusculas += 1

            if empieza_vocal and tiene_b:
                if palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b is None:
                    palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b = cant_de_letras_por_palabra
                elif cant_de_letras_por_palabra > palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b:
                    palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b = cant_de_letras_por_palabra

            if cant_consonantes > cant_vocales and not tiene_a and not tiene_m:
                cant_palabras_que_tienen_mas_consonantes_que_vocales_y_no_tienen_a_o_m += 1
                cant_letras_de_palabras_que_tienen_mas_consonantes_que_vocales_y_no_tienen_a_o_m += cant_de_letras_por_palabra

            if cant_d >= 2 and es_vocal(anterior):
                cant_palabras_incluyen_dos_o_mas_veces_d_y_vocal_y_terminan_en_vocal += 1



            # RESETEO FLAGS R1
            cant_de_letras_por_palabra = 0
            empieza_digito_impar = False
            tiene_letras_minusculas_dsp_del_digito = True

            #RESETEO FLAGS R2
            empieza_vocal = tiene_b = False

            #RESETEO FLAGS R3
            cant_vocales = cant_consonantes = 0
            tiene_a = tiene_m = False

            #RESETEP FLAGS R4
            cant_d = 0


        else:
            cant_de_letras_por_palabra += 1
            cant_letras_totales_en_texto += 1

            if es_digito(letra):
                if cant_de_letras_por_palabra == 1 and es_impar(letra):
                    empieza_digito_impar = True

            elif es_consonante(letra):
                cant_consonantes += 1
                if letra == 'b' or letra == 'B':
                    tiene_b = True
                if letra == 'm' or letra == 'M':
                    tiene_m = True

            elif es_vocal(letra):
                cant_vocales += 1
                if cant_de_letras_por_palabra == 1:
                    empieza_vocal = True
                if letra == 'a' or letra == 'A':
                    tiene_a = True
                if anterior == 'd' or anterior == 'D':
                    cant_d += 1

            if cant_de_letras_por_palabra == 2 and es_minuscula(letra):
                tiene_letras_minusculas_dsp_del_digito = True

            elif not es_minuscula(letra):
                tiene_letras_minusculas_dsp_del_digito = False

            anterior = letra


    r1 = cant_palabras_empiezan_digito_siguen_con_minusculas
    r2 = palabra_mas_larga_que_comienza_voca_y_tiene_al_menos_una_b
    r3 = promedio_entero(cant_letras_de_palabras_que_tienen_mas_consonantes_que_vocales_y_no_tienen_a_o_m, cant_palabras_que_tienen_mas_consonantes_que_vocales_y_no_tienen_a_o_m)
    r4 = cant_palabras_incluyen_dos_o_mas_veces_d_y_vocal_y_terminan_en_vocal


    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)



if __name__ == '__main__':
    principal()
