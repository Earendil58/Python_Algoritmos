nombre_primer_producto = input('Ingrese el nombre del primer producto: ')
cantidad_primer_producto = int(input('Ingrese la cant vendida del primer articulo: '))
precio_unitario_primero = float(input('Ingrese el precio unitario del primer articulo: '))

nombre_segundo_producto = input('Ingrese el nombre del segundo producto: ')
cantidad_segundo_producto = int(input('Ingrese la cant vendida del segundo articulo: '))
precio_unitario_segundo = float(input('Ingrese el precio unitario del segundo articulo: '))

nombre_tercer_producto = input('Ingrese el nombre del tercer producto: ')
cantidad_tercer_producto = int(input('Ingrese la cant vendida del tercer articulo: '))
precio_unitario_tercero = float(input('Ingrese el precio unitario del tercer articulo: '))


#CALCULAMOS PRECIO TOTAL DE VENTAS DE CADA ARTICULO

precio_total_primer_articulo    = cantidad_primer_producto * precio_unitario_primero
precio_total_segundo_articulo   = cantidad_segundo_producto * precio_unitario_segundo
precio_total_tercer_articulo    = cantidad_tercer_producto * precio_unitario_tercero

#CUAL ES EL QUE GENERO VENTAS MÁS ALTAS

if precio_total_primer_articulo > precio_total_segundo_articulo and precio_total_primer_articulo > precio_total_tercer_articulo:
    precio_total_mas_alto = precio_total_primer_articulo
    nombre_articulo_mas_alto = nombre_primer_producto

elif precio_total_segundo_articulo > precio_total_primer_articulo and precio_total_segundo_articulo > precio_total_tercer_articulo:
    precio_total_mas_alto = precio_total_segundo_articulo
    nombre_articulo_mas_alto = nombre_segundo_producto

else:
    precio_total_mas_alto = precio_total_tercer_articulo
    nombre_articulo_mas_alto = nombre_tercer_producto

#CALCULO EL PRECIO TOTAL DE LAS VENTAS COMBINADAS

ventas_totales = precio_total_primer_articulo + precio_total_segundo_articulo + precio_total_tercer_articulo

#CALCULO EL PORCENTAJE QUE REALIZÓ EL MAYOR APORTANTE

porcentaje_mayor_ventas_sobre_total_vendido = round(((precio_total_mas_alto * 100) / ventas_totales),2)

print(f'El porcentaje de mayor ventas fue del articulo: ${precio_total_mas_alto}, que vino de el articulo: {nombre_articulo_mas_alto},'
      f' sobre el total vendido fue de: {porcentaje_mayor_ventas_sobre_total_vendido}%')
