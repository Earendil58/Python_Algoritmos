letra = input("Digite uma letra: ")

if "a" < letra < "z":
    print('El caracter es una letra minúscula')

elif "A" < letra < "Z":
    print(f'El caracter ingresado {letra} es una letra mayúscula')

else:
    print(f'El caracter ingresado {letra} no es una letra')