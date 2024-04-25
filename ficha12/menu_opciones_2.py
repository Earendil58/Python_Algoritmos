def impares_multiplos_tres(limite_derecho):
    impares_multiplos_tres =  []
    for numero in range(1,limite_derecho + 1):
       if (numero % 2 != 0) and (numero % 3 == 0):
           impares_multiplos_tres.append(numero)

    return impares_multiplos_tres


def numero_primo_en_intervalo(a,b):
    if a > 1 and b > a:
        es_primo = True
        primos = []
        for numero in range(a, b + 1):
            for divisor in range(2, b):
                if numero % divisor == 0:
                    es_primo = False
            if es_primo:
                primos.append(numero)
    else:
        print('Los valores proporcionados deben ser positivos. B debe ser mayor que A.')





def test():
    #MOSTRAR LAS OPCIONES DE MENU
    print('Ingrese alguna de las siguientes opciones:')
    print('-' * 150)
    print('1) Chequear todos los números impares y múltiplos de 3.')
    print('2) Cargar dos números y chequear si existe algún número primo dento de su intervalo cerrado, si existe, mostrarlo.')
    print('3) Cargar una secuencia de números, cortar el proceso cuando el número cargado sea el 0, ordenar los números cargados de menor a mayor.')
    print('-' * 150)

    opcion = - 1

    while opcion > 3 or opcion < 1:
        opcion = int(input('Ingrese una opción de las que se presentaron: '))
        print('-' * 150)

    if opcion == 1:
        limite = int(input('Ingrese un limite para chequear impares y múltiplos de 3, en el intervalo: '))
        output_opcion_uno = impares_multiplos_tres(limite)
        print(output_opcion_uno)




test()



