
def es_primo(numero):
    primo = False
    if numero < 1:
        primo = False
    elif numero == 1:
        primo = False
    elif numero == 2:
        primo = True
    elif numero % 2:
        primo = False

    raiz = int(pow(numero, 0.5))

    for divisor in range(3,raiz + 1, 2):
        if numero % divisor == 0:
            primo = False

    primo = True

    if primo:
        print(f'El número:{numero} es primo')
    else:
        print(f'El número: {numero} no es primo')


es_primo(10000000000061)



