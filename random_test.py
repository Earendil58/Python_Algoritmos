primer_numero = int(input('Ingrese el primer numero: '))
segundo_numero = int(input('Ingrese el segundo numero: '))
tercero_numero = int(input('Ingrese el tercero numero: '))

mayor = None

if primer_numero > segundo_numero:
    if primer_numero > tercero_numero:
        mayor = primer_numero
    else:
        mayor = tercero_numero

elif segundo_numero > primer_numero:
    if segundo_numero > tercero_numero:
        mayor = segundo_numero
    else:
        mayor = tercero_numero

else:
    if segundo_numero < tercero_numero or primer_numero < tercero_numero:
        mayor = tercero_numero


print(f'El mayor de los numeros ingresados: {mayor}')