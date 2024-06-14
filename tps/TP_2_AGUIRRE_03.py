def leer_archivo():
    with open('envios100HC.txt', 'rt') as tratar_archivo:
        texto = tratar_archivo.read()
    return texto


def detectar_tipo_control(texto):
    tipo_control = texto.split('\n', 1)[0]  # Obtener la primera línea
    if 'HC' in tipo_control:
        return 'Hard Control'
    elif 'SC' in tipo_control:
        return 'Soft Control'
    return ''


def obtener_linea(texto, inicio):
    linea = ''
    while inicio < len(texto) and texto[inicio] != '\n':
        linea += texto[inicio]
        inicio += 1
    return linea.strip(), inicio + 1


def procesar_linea_envio(linea_envio):
    if len(linea_envio) < 31:
        return None, None, None, None
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
        contiene_digitos = False
        anterior = ''
        es_palabra = False
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
            if letra in ' -/#.':
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
    precios_base = [1100, 1800, 2450, 8300, 10900, 14300, 17900]
    precio_base = precios_base[tipo_envio] if tipo_envio < len(precios_base) else 0

    pais = determinar_pais(codigo_postal)
    if pais != 'Argentina':
        if pais in ['Bolivia', 'Paraguay', 'Uruguay']:
            precio_base *= 1.2
        elif pais in ['Chile', 'Brasil']:
            precio_base *= 1.25
        else:
            precio_base *= 1.5

    return precio_base


def determinar_pais(codigo_postal):
    if codigo_postal and '0' <= codigo_postal[0] <= '9':
        return 'Argentina'
    return 'Otro'


def determinar_provincia(codigo_postal):
    if codigo_postal and codigo_postal[0] == 'B':
        return 'Buenos Aires'
    return 'Otra'


def main():
    texto = leer_archivo()
    tipo_control = detectar_tipo_control(texto)
    indice = texto.find('\n') + 1  # Saltar la línea de tipo de control

    # Variables de estadísticas
    validos, invalidos, total_importe = 0, 0, 0
    cartas_simples, cartas_certificadas, cartas_expresas = 0, 0, 0
    primer_cp, contador_primer_cp = "", 0
    menor_importe_brasil = float('inf')
    cp_menor_importe_brasil = ""
    total_envios, total_envios_exterior = 0, 0
    total_importe_buenos_aires, envios_buenos_aires = 0, 0

    while indice < len(texto):
        linea, nuevo_indice = obtener_linea(texto, indice)
        indice = nuevo_indice

        if linea == '':
            continue

        cp, direccion, tipo_envio, forma_pago = procesar_linea_envio(linea)
        if cp is None:
            continue

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

            if not primer_cp:
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

    porcentaje_exterior = (total_envios_exterior * 100) // total_envios if total_envios else 0
    promedio_buenos_aires = total_importe_buenos_aires // envios_buenos_aires if envios_buenos_aires else 0

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
