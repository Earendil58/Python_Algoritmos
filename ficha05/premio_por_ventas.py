primer_monto = float(input('Ingrese el monto del primer vendedor: '))

segundo_monto = float(input('Ingrese el monto del segundo vendedor: '))

tercer_monto = float(input('Ingrese el monto del tercer vendedor: '))

mejor_vendedor = max(primer_monto, segundo_monto, tercer_monto)

#CALCULAR EL MENOR MONTO VENDIDO

if primer_monto < segundo_monto and primer_monto < tercer_monto:
    menor_monto = primer_monto

elif segundo_monto < primer_monto and segundo_monto < tercer_monto:
    menor_monto = segundo_monto

else:
    menor_monto = tercer_monto

cincuenta_por_ciento_de_menor_monto = menor_monto * 0.5

#SI ALGUNO DE LOS MONTOS SUPERA LOS $1000

if primer_monto > 1000 and segundo_monto > 1000 and tercer_monto > 1000:
    cincuenta_por_ciento_de_menor_monto += cincuenta_por_ciento_de_menor_monto * 0.1

print(f'El premio al mejor vendedor es de: {cincuenta_por_ciento_de_menor_monto}, se le otorga al vendedor que vendió: {mejor_vendedor}')
