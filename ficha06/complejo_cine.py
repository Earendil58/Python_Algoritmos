cant_espectadores = int(input('Ingrese cantidad de espectadores (recuerde que si presiona 0, se termina el programa) :'))
recaudacion = 0
funciones_dto = 0
funciones_totales = 0



while cant_espectadores != 0:
    descuento = input('Posee descuento? (S/N): ')
    descuento = descuento.lower()
    if descuento == 's':
        recaudacion += cant_espectadores * 50
        funciones_dto += 1
    else:
        recaudacion += cant_espectadores * 75


    funciones_totales += 1
    cant_espectadores = int(input('Ingrese cantidad de espectadores (recuerde que si presiona 0, se termina el programa) :'))


porcentaje_funciones_descuento = round(((funciones_dto * 100) / funciones_totales), 2)

print(f'La recaudación total fue de: {recaudacion}, las funciones con dto fueron: {funciones_dto}')
print(f'El porcentaje de funciones con descuentos fue del: {porcentaje_funciones_descuento}%')
