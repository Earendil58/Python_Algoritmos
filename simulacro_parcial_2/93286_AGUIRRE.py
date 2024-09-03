def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'

def es_mayuscula(caracter):
    return 'A' <= caracter <= 'Z'

def es_vocal(caracter):
    return caracter in 'aeiouáéíóúAEIOUÁÉÍÓÚ'

def es_digito(caracter):
    return '0' <= caracter <= '9'

def promedio_entero(cant_letras, cant_palabras):
    promedio = 0
    if cant_letras > 0 and cant_palabras > 0:
        promedio = cant_letras // cant_palabras
    return promedio



def principan():
    tratar_archivo = open('entrada.txt')
    texto = tratar_archivo.read()
    tratar_archivo.close()

    # R1 FLAGS
    cant_letras_por_palabra = 0
    comienza_mayuscula = False
    cant_palabras_comienzan_mayuscula_y_tienen_digito_en_cuanto_pos = 0
    tiene_digito_en_cuarto_lugar = False

    # R2 FLAGS
    palabra_mas_larga_tiene_p_o_n = None
    tiene_p = False
    tiene_n = False

    # R3 FLAGS
    cant_veces_tuvo_digito = 0
    tiene_vocal_r3 = False
    cant_caracteres_palabra_tuvo_dos_o_mas_digitos_y_una_vocal = 0
    cant_palabras_tuvo_dos_o_mas_digitos_y_una_vocal = 0

    # R4 FLAGS
    comienza_vocal = False
    tiene_f = False
    tiene_a = False
    cant_palabras_comienzan_vocal_y_tienen_fa = 0

    for letra in texto:
        if letra == ' ' or letra == '.':
            if comienza_mayuscula and tiene_digito_en_cuarto_lugar:
                cant_palabras_comienzan_mayuscula_y_tienen_digito_en_cuanto_pos += 1

            if comienza_vocal and tiene_f and tiene_a:
                cant_palabras_comienzan_vocal_y_tienen_fa += 1

            if tiene_p or tiene_n:
                if palabra_mas_larga_tiene_p_o_n is None:
                    palabra_mas_larga_tiene_p_o_n = cant_letras_por_palabra
                elif cant_letras_por_palabra > palabra_mas_larga_tiene_p_o_n:
                    palabra_mas_larga_tiene_p_o_n = cant_letras_por_palabra

            if cant_veces_tuvo_digito >= 2 and tiene_vocal_r3:
                cant_caracteres_palabra_tuvo_dos_o_mas_digitos_y_una_vocal += cant_letras_por_palabra
                cant_palabras_tuvo_dos_o_mas_digitos_y_una_vocal += 1

            # RESETEO FLAGS R1
            comienza_mayuscula = tiene_digito_en_cuarto_lugar = False
            cant_letras_por_palabra = 0

            # RESETEO FLAGS R2
            tiene_p = tiene_n = False

            # RESETEO FLAGS R3
            cant_veces_tuvo_digito = 0
            tiene_vocal_r3 = False

            # RESETEO FLAGS R4
            tiene_f = tiene_a = comienza_vocal = False


        else:
            cant_letras_por_palabra += 1

            if es_letra(letra):
                if cant_letras_por_palabra == 1 and es_mayuscula(letra):
                    comienza_mayuscula = True

                if comienza_vocal and (letra == 'f' or letra == 'F'):
                    tiene_f = True

                if comienza_vocal and (anterior == 'f' or anterior == 'F'):
                    if letra == 'a' or letra == 'A' or letra == 'á' or letra == 'Á':
                        tiene_a = True

                if letra == 'p' or letra == 'P':
                    tiene_p = True
                if letra == 'n' or letra == 'N':
                    tiene_n = True

            if es_vocal(letra):
                tiene_vocal_r3 = True

                if cant_letras_por_palabra == 1:
                    comienza_vocal = True

            if es_digito(letra):
                cant_veces_tuvo_digito += 1

                if cant_letras_por_palabra == 4:
                    tiene_digito_en_cuarto_lugar = True

            anterior = letra

        # LOS CALCULOS Y ASIGNACIONES FINALES DEBE HACERLOS FUERA DEL CICLO
        promedio_entero_r3 = promedio_entero(cant_caracteres_palabra_tuvo_dos_o_mas_digitos_y_una_vocal, cant_palabras_tuvo_dos_o_mas_digitos_y_una_vocal)


        r1 = cant_palabras_comienzan_mayuscula_y_tienen_digito_en_cuanto_pos
        r2 = palabra_mas_larga_tiene_p_o_n
        r3 = promedio_entero_r3
        r4 = cant_palabras_comienzan_vocal_y_tienen_fa


    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principan()
