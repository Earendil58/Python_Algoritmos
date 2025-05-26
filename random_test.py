#Diseña un programa que, dado un número entero, determine si este es el doble de un número impar. (Ejemplo: 14 es el doble de 7, que es impar).

numero = float(input("Digite um numero: "))

if not numero.is_integer():
    print("El número ingresado no es entero.")

if numero % 2 == 0:
    if (numero // 2) % 2 != 0:
        print(f"El número {numero} es el doble de impar")

    elif (numero // 2) % 2 == 0:
        print(f'El número {numero} es par pero no es doble de impar')

else:
    print(f'El número {numero} es impar')



