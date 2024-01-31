texto = input('Ingrese un texto: ')

contador_espacios = 0
caracter_anterior = ' '
palabras = 0
letra_inicial_p = 0

for caracter in texto:


    if caracter != ' ' and caracter_anterior == ' ':
        palabras += 1
        if caracter == 'p' or caracter == 'P':
            letra_inicial_p += 1


    caracter_anterior = caracter




print(f'La cantidad de palabras ingresadas es: {palabras}')
print(f'La cantidad de palabras que empiezan con las letra "p" son: {letra_inicial_p}')
