# Desarrolle un programa o script Python que permita cargar por teclado un número entero
# que representa la  cantidad de segundos que pasaron desde un evento dado.
# El programa debe convertir esa cantidad de segundos  a la cantidad de horas, minutos y segundos que transcurrieron.
# Por ejemplo, si la cantidad de segundos  ingresada es 4452 deberá mostrar un mensaje que informe
# que el tiempo transcurrido fue de 1 hora, 14 minutos  y 12 segundos. Pero la conversión solo debe mostrarse si la cantidad de horas totales
# obtenida es menor o igual a 24. Si esa cantidad de horas totales es mayor a 24, el programa debe mostrar un mensaje de la forma "Excedido".
# Se le pedirá comprobar su programa para cuatro cantidades de segundos, que deberá cargar por teclado.
#
# Además, el desafío incluye una consigna adicional, en la cual se le pedirá que haga el proceso inverso: deberá tomar tres datos,
# que serán el valor en horas, el valor en minutos y el valor en segundos transcurridos desde un evento dado,
# y su programa deberá calcular la cantidad total de segundos a partir de esos datos.
# Por ejemplo, si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 entonces el resultado a obtener es que la cantidad total de
# segundos es 16568.

cant_segundos = int(input('Ingrese el número de segundos transcurridos desde el evento: '))

if cant_segundos < 86400:
    horas = cant_segundos // 3600
    minutos = (cant_segundos % 3600) // 60
    segundos = ((cant_segundos % 3600) % 60)

    print(f'Horas: {horas}')
    print(f'Minutos: {minutos}')
    print(f'Segundos: {segundos}')

else:
    print('Excedido')



# -----------        SEGUNDA PARTE           ---------------------------------------------------------

horas = int(input('Ingrese la cantidad de horas: '))
minutos = int(input('Ingrese la cantidad de minutos: '))
segundos = int(input('Ingrese la cantidad de segundos: '))

horas_a_segundos = horas * 60 * 60
minutos_a_segundos = minutos * 60

cant_total_en_segundos = horas_a_segundos + minutos_a_segundos + segundos

print(cant_total_en_segundos)
