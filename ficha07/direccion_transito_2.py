

patente = input('Ingrese su patente: ')

if len(patente) == 6:
    formato_ok = True
    posicion = 0

    for caracter in patente:
        posicion += 1

        if 1 <= posicion <= 3:
            if 'A' > caracter > 'Z' or 'a'> caracter > 'z':
                formato_ok = False

        elif 4 <= posicion <= 6:
            if '1' > caracter > '9':
                formato_ok = False

        else:
            print(f'El formato de la parente es viejo, tiene {len(patente)} y el formato es correcto')

elif len(patente) == 7:
    formato_ok = True
    posicion = 0

    for caracter in patente:
        posicion += 1

        if 1 <= posicion <= 2:
            if 'A' > caracter > 'Z' or 'a' > caracter > 'z':
                formato_ok = False

        elif 3 <= posicion <= 5:
            if '1' < caracter > '9':
                formato_ok = False

        elif 5 <= posicion <= 7:
            if 'A' > caracter > 'Z' or 'a' > caracter > 'z':
                formato_ok = False

        else:
            print(f'El formato de la patente es el actual, tiene {len(patente)} caracteres y el formato es correcto')


else:
    print(f'La patente tiene una longitud inválida, tiene: {len(patente)} caracteres')
