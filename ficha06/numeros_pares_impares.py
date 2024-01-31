
numero = float(input('Ingrese un número: '))

num_entre_50_y_100 = 0
cant_valores_pares = 0
cant_valores_impares = 0
al_menos_un_num_0 = False
anterior = None
par_impar_continuo = True
par = 0
impar = 0


while numero >= 0:

    if 50 <= numero <= 100:
        num_entre_50_y_100 += 1

    if numero % 2 == 0:
        cant_valores_pares += 1

    else:
        cant_valores_impares += 1


    if numero == 0:
        al_menos_un_num_0 = True

    if anterior == None:
        if numero % 2 != 0:
            par_impar_continuo = False
        else:
            anterior = numero

    paridad = numero % 2
    if paridad == anterior:
        par_impar_continuo = False




    numero = float(input('Ingrese un número: '))


if al_menos_un_num_0:
    print('Se ingresó al menos un número 0')


if par_impar_continuo:
    print('Ingresaste un número par, seguido de un impar en cada iteración')



print(f'La cantidad de números comprendidos entre 50 y 100 fue de: {num_entre_50_y_100}')
print(f'La cantidad de valores pares, fue de: {cant_valores_pares}')
print(f'La cantidad de valores impares, fue de: {cant_valores_impares}')

