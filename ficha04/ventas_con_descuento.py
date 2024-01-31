precio_unitario = float(input('Ingrese el precio unitario: '))
cantidad_vendida = int(input('Ingrese la cantidad de producto vendida: '))
pago_efectivo = input('Se pago en efectivo ? SI / NO: ')

pago_efectivo = pago_efectivo.lower()

precio_final = precio_unitario * cantidad_vendida
precio_con_descuento = precio_final

if pago_efectivo == 'si' and cantidad_vendida > 10:
    precio_con_descuento = precio_final * 0.85
else:
    precio_con_descuento = precio_final * 0.95

print(f'El precio final es {precio_final} y el precio con descuento es: {precio_con_descuento}')


