fecha_cadena = input('Ingrese una fecha: ')


dia = fecha_cadena[0] + fecha_cadena[1]
mes = fecha_cadena[3] + fecha_cadena[4]
anio = fecha_cadena[6] + fecha_cadena[7] + fecha_cadena[8] + fecha_cadena[9]

print('Día: {} - Mes: {} - Año: {}'.format(dia, mes, anio))
