#INGRESO POR TECLADO

cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

#NORMALIZAR LETRAS CP
cp = cp.upper()

#VARIABLES AUXILIARES
letras = 'ABCDEFGHJKLMNPQRSTUVWXYZ' #LETRAS I/O NO SE UTILIZAN
numeros = '0123456789'
longitud_cp = len(cp)
destino = ''

if 4 < longitud_cp > 9:
    destino = 'Otro'

else:
    if longitud_cp == 8:
        if (cp[0] in letras) and (cp[1] in numeros) and (cp[2] in numeros) and (cp[3] in numeros) and (cp[4] in numeros) and (cp[5] in letras) and (cp[6] in letras) and (cp[7] in letras):
            destino = 'Argentina'
        else:
            destino = 'Otro'

    elif longitud_cp == 4:
        if (cp[0] in numeros) and (cp[1] in numeros) and (cp[2] in numeros) and (cp[3] in numeros):
            destino = 'Bolivia'
        else:
            destino = 'Otro'

    elif longitud_cp == 9:
        if (cp[0] in numeros) and (cp[1] in numeros) and (cp[2] in numeros) and (cp[3] in numeros) and (cp[4] in numeros) and (cp[5] == '-') and (cp[6] in numeros) and (cp[7] in numeros) and (cp[8] in numeros):
            destino = 'Brasil'
        else:
            destino = 'Otro'

    elif longitud_cp == 7:
        if (cp[0] in numeros) and (cp[1] in numeros) and (cp[2] in numeros) and (cp[3] in numeros) and (cp[4] in numeros) and (cp[5] in numeros) and (cp[6] in numeros):
            destino = 'Chile'
        else:
            destino = 'Otro'

    elif longitud_cp == 6:
        if (cp[0] in numeros) and (cp[1] in numeros) and (cp[2] in numeros) and (cp[3] in numeros) and (cp[4] in numeros) and (cp[5] in numeros):
            destino = 'Paraguay'
        else:
            destino = 'Otro'

    elif longitud_cp == 5:
        if (cp[0] in numeros) and (cp[1] in numeros) and (cp[2] in numeros) and (cp[3] in numeros) and (cp[4] in numeros):
            destino = 'Uruguay'
        else:
            destino = 'Otro'






print("País de destino del envío:", destino)
