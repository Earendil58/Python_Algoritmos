# Desarrollar un programa en Python que permita cargar por teclado un texto
# completo (analizar dos opciones: una es cargar todo el texto en una variable de tipo cadena
# de caracteres y recorrerla con un for iterador; y la otra es cargar cada caracter uno por uno a
# través de un while). Siempre se supone que el usuario cargará un punto para indicar el final
# del texto, y que cada palabra de ese texto está separada de las demás por un espacio en
# blanco. El programa debe:
# a. Determinar cuántas palabras se cargaron.
# b. Determinar cuántas palabras comenzaron con la letra "p".
# c. Determinar cuántas palabras contuvieron una o más veces la expresión "ta".

texto = input('Ingrese un texto: ')

texto_normalizado = texto.lower()

cant_letras = 0
es_primera_letra = True
palabras_en_texto = 0
comienza_p = 0
tuvieron_ta = 0
letra_anterior = ''
letra_p = False
letra_a = False
aparecio_ta = False

for letra in texto_normalizado:

    cant_letras += 1

    if letra == ' ' or letra == '.':
        if cant_letras > 1:
            palabras_en_texto += 1

        es_primera_letra = True
        cant_letras = 0
        aparecio_ta = False

    else:
        if cant_letras == 1 and letra == 'p':
            comienza_p += 1
            es_primera_letra = False

        if letra_anterior == 't' and letra == 'a' and not(aparecio_ta):
            tuvieron_ta += 1
            aparecio_ta = True

    letra_anterior = letra


print(f'El texto tiene: {palabras_en_texto} palabras')
print(f'El texto tiene: {comienza_p} palabras que empiezan con "p"')
print(f'El texto tiene: {tuvieron_ta} palabras con la sílaba "ta" en ella')
