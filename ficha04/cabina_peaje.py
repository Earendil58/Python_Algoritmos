import random

numero_sorteado = random.randint(1,9)

patente = int(input('Ingrese la patente de su vehiculo: '))

descuento = 0
ultimo_digito_patente = patente % 10

if ultimo_digito_patente == numero_sorteado:
    tarifa = 50
else:
    tarifa = 90


if ultimo_digito_patente == 7:
    tarifa = tarifa * 0.5
    print('entro en el descuento del 50', descuento)
else:
    tarifa = tarifa * 0.9

print(f'El monto a pagar es de {tarifa}, ya que el número sorteado fue: {numero_sorteado} y el último número \
de su patente es: {ultimo_digito_patente}')
