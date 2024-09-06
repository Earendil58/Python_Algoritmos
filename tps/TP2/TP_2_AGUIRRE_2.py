def leer_archivo():
    tratar_archivo = open('envios100HC.txt', 'rt')
    texto = tratar_archivo.read()
    tratar_archivo.close()
    return texto


def detectar_tipo_control(texto):
    indice = 0
    control_detectado = ''
    tipo_de_control = ''
    while indice < len(texto):
        if texto[indice] == '\n':
            break
        control_detectado += texto[indice]
        indice += 1
    if 'HC' in control_detectado:
        tipo_de_control = 'Hard Control'
    elif 'SC' in control_detectado:
        tipo_de_control = 'Soft Control'

    return tipo_de_control


def obtener_linea(texto, inicio):
    linea = ''
    while inicio < len(texto) and texto[inicio] != '\n':
        linea += texto[inicio]
        inicio += 1
    return linea, inicio + 1


def procesar_linea_envio(linea_envio):
    codigo_postal = linea_envio[:9].strip()
    direccion = linea_envio[9:29].strip()
    tipo_envio = int(linea_envio[29])
    forma_pago = int(linea_envio[30])
    return codigo_postal, direccion, tipo_envio, forma_pago


def validar_direccion(direccion, tipo_control):
    if tipo_control == 'Hard Control':
        tiene_letras_y_digitos = False
        no_mayusculas_consecutivas = True
        palabra_digitos = False
        anterior = ''
        es_palabra = False
        contiene_digitos = False
        indice = 0

        while indice < len(direccion):
            letra = direccion[indice]
            if '0' <= letra <= '9':
                contiene_digitos = True
                es_palabra = True
            if ('a' <= letra <= 'z') or ('A' <= letra <= 'Z'):
                tiene_letras_y_digitos = True
                es_palabra = True
                if 'A' <= anterior <= 'Z' and 'A' <= letra <= 'Z':
                    no_mayusculas_consecutivas = False
            if letra == ' ' or letra == '-' or letra == '/' or letra == '#' or letra == '.':
                if es_palabra and contiene_digitos:
                    palabra_digitos = True
                es_palabra = False
                contiene_digitos = False
            anterior = letra
            indice += 1

        return tiene_letras_y_digitos and no_mayusculas_consecutivas and palabra_digitos
    elif tipo_control == 'Soft Control':
        return True
    return False


def calcular_precio(tipo_envio, codigo_postal):
    if tipo_envio == 0:
        precio_base = 1100
    elif tipo_envio == 1:
        precio_base = 1800
    elif tipo_envio == 2:
        precio_base = 2450
    elif tipo_envio == 3:
        precio_base = 8300
    elif tipo_envio == 4:
        precio_base = 10900
    elif tipo_envio == 5:
        precio_base = 14300
    elif tipo_envio == 6:
        precio_base = 17900

    pais = determinar_pais(codigo_postal)
    if pais != 'Argentina':
        if pais == 'Bolivia' or pais == 'Paraguay' or pais == 'Uruguay':
            precio_base *= 1.2
        elif pais == 'Chile' or pais == 'Brasil':
            precio_base *= 1.25
        else:
            precio_base *= 1.5

    return precio_base


def determinar_pais(codigo_postal):
    if '0' <= codigo_postal[0] <= '9':
        return 'Argentina'
    return 'Otro'


def determinar_provincia(codigo_postal):
    if codigo_postal != '' and codigo_postal[0] == 'B':
        return 'Buenos Aires'
    return 'Otra'


def main():
    texto = leer_archivo()
    tipo_control_texto = detectar_tipo_control(texto)

    tipo_control = tipo_control_texto
    indice = 0
    validos = 0
    invalidos = 0
    total_importe = 0
    cartas_simples = 0
    cartas_certificadas = 0
    cartas_expresas = 0
    primer_cp = ""
    contador_primer_cp = 0
    menor_importe_brasil = 9999999
    cp_menor_importe_brasil = ""
    total_envios = 0
    total_envios_exterior = 0
    total_importe_buenos_aires = 0
    envios_buenos_aires = 0

    while indice < len(texto):
        linea, nuevo_indice = obtener_linea(texto, indice)
        indice = nuevo_indice

        if linea == '':
            continue

        cp, direccion, tipo_envio, forma_pago = procesar_linea_envio(linea)
        es_valido = validar_direccion(direccion, tipo_control)

        if es_valido:
            validos += 1
            precio = calcular_precio(tipo_envio, cp)
            total_importe += precio

            if tipo_envio == 0:
                cartas_simples += 1
            elif tipo_envio == 1:
                cartas_certificadas += 1
            elif tipo_envio == 2:
                cartas_expresas += 1

            if primer_cp == "":
                primer_cp = cp
                contador_primer_cp = 1
            elif primer_cp == cp:
                contador_primer_cp += 1

            if determinar_pais(cp) == 'Brasil' and precio < menor_importe_brasil:
                menor_importe_brasil = precio
                cp_menor_importe_brasil = cp

            if determinar_provincia(cp) == 'Buenos Aires':
                total_importe_buenos_aires += precio
                envios_buenos_aires += 1

            if determinar_pais(cp) != 'Argentina':
                total_envios_exterior += 1

        else:
            invalidos += 1

        total_envios += 1

    tipo_carta_mayor_envios = 'Carta Simple'
    if cartas_certificadas > cartas_simples and cartas_certificadas > cartas_expresas:
        tipo_carta_mayor_envios = 'Carta Certificada'
    elif cartas_expresas > cartas_simples and cartas_expresas > cartas_certificadas:
        tipo_carta_mayor_envios = 'Carta Expresa'

    if total_envios > 0:
        porcentaje_exterior = (total_envios_exterior * 100) // total_envios
    else:
        porcentaje_exterior = 0

    if envios_buenos_aires > 0:
        promedio_buenos_aires = total_importe_buenos_aires // envios_buenos_aires
    else:
        promedio_buenos_aires = 0

    print("Tipo de Control:", tipo_control)
    print("Envíos válidos:", validos)
    print("Envíos inválidos:", invalidos)
    print("Importe total:", total_importe)
    print("Cartas Simples:", cartas_simples)
    print("Cartas Certificadas:", cartas_certificadas)
    print("Cartas Expresas:", cartas_expresas)
    print("Tipo de carta con mayor envíos:", tipo_carta_mayor_envios)
    print("Primer CP:", primer_cp)
    print("Veces que apareció el primer CP:", contador_primer_cp)
    print("Menor importe a Brasil:", menor_importe_brasil)
    print("CP menor importe a Brasil:", cp_menor_importe_brasil)
    print("Porcentaje de envíos al exterior:", porcentaje_exterior)
    print("Promedio de envíos a Buenos Aires:", promedio_buenos_aires)


main()
