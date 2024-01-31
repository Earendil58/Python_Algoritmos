
numero = int(input('Ingrese un número: '))

mismo_signo = True
signo_negativo = False
signo_positivo = False
numeros_ingresados = []


while numero != 0:
    numeros_ingresados.append(numero)


    if numero > 0:
        signo_positivo = True

    else:
        signo_negativo = True

    if numero > 0 and signo_negativo:
        mismo_signo = False

    elif numero < 0 and signo_positivo :
        mismo_signo = False

    numero = int(input('Ingrese un número: '))



if mismo_signo:
    print(f'Los números ingresados son todos de igual signo: {numeros_ingresados}')

else:
    print(f'Los números ingresados no son todos de igual signo: {numeros_ingresados}')
