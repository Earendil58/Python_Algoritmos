numero_uno = int(input("Digite el primer numero: "))
numero_dos = int(input("Digite el segundo numero: "))

cuadrado_del_primero = numero_uno ** 2

if cuadrado_del_primero == numero_dos:
    print(f"El segundo numero {numero_dos} es el cuadrado del primer numero {numero_uno}")

elif cuadrado_del_primero < numero_dos:
    print(f'El cuadrado del primero es menor al segundo numero {numero_dos}')

else:
    print(f'El cuadrado del primero es mayor al segundo numero {numero_dos}')