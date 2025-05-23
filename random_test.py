#Diseña un programa que, dado un número entero, determine si este es el doble de un número impar. (Ejemplo: 14 es el doble de 7, que es impar).

numero = float(input("Digite um numero: "))
divisores = numero - 1
divisor = None
impar_doble_de_par = False

#NUMERO POSITIVO E IMPAR:
if numero > 0 and numero % 2 != 0:
    while numero % divisores != 0:
        divisores -= 1

    divisor = divisores

    if divisores == 1:
        impar_doble_de_par = True
    else:
        print(f'El número {numero} es impar. No es doble de impares')



 #NUMERO PAR
else:
    print(f'El número: {numero} es par, por lo que no es el doble de un número impar')


if impar_doble_de_par:
    print(f'El número: {numero} es impar, doble de par.')


