primer_numero = float(input('Ingrese el primer número: '))
segundo_numero = float(input('Ingrese el segundo número: '))
tercer_numero = float(input('Ingrese el tercer número: '))


suma = primer_numero + segundo_numero + tercer_numero

if suma > 10 :
    dividido = suma // 2
    print(f'El resultado dividido por dos, sin decimales, es: {dividido}')
else:
    cubo = suma ** 3
    print(f'El resultado de la suma de los 3 números al cubo es: {cubo}')
