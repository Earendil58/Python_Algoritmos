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
def obtener_indice(texto, inicio):
    omitir_primera_linea = True
    if omitir_primera_linea:
        while inicio < len(texto) and texto[inicio] != '\n':
            inicio += 1
        inicio += 1
    while inicio < len(texto) and texto[inicio] != '\n':
        inicio += 1
    if inicio < len(texto):
        inicio += 1
    return inicio
def validar_direccion(direccion, tipo_de_control):
    if tipo_de_control == 'Hard Control':
        tiene_letras_y_digitos = False
        no_mayusculas_consecutivas = True
        palabra_digitos = False
        anterior = ''
        es_palabra = False
        contiene_digitos = False
        for letra in direccion:
            if letra.isdigit():
                contiene_digitos = True
                es_palabra = True
            elif letra.isalpha():
                tiene_letras_y_digitos = True
                es_palabra = True
                if anterior.isupper() and letra.isupper():
                    no_mayusculas_consecutivas = False
            elif letra in ' -/#.':
                if es_palabra and contiene_digitos:
                    palabra_digitos = True
                es_palabra = False
                contiene_digitos = False
            anterior = letra
        if tiene_letras_y_digitos and no_mayusculas_consecutivas and palabra_digitos:
            return True
        else:
            return False
    else:
        return False
def calcular_precio(tipo_envio, cod_postal):
    precio_base = 0
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
    pais = determinar_pais(cod_postal)
    if pais == 'Argentina':
        pass
    else:
        if pais == 'Bolivia' or pais == 'Paraguay' or (pais == 'Uruguay' and cod_postal[0] == '1'):
            precio_base *= 1.2
        elif pais == 'Chile' or (pais == 'Uruguay' and cod_postal[0] != '1'):
            precio_base *= 1.25
        elif pais == 'Brasil':
            if '0' <= cod_postal[0] <= '3':
                precio_base *= 1.25
            elif '4' <= cod_postal[0] <= '7':
                precio_base *= 1.3
            elif '8' <= cod_postal[0] <= '9':
                precio_base *= 1.2
        else:
            precio_base *= 1.5
    return int(precio_base)
def determinar_pais(cod_postal):
    lcp = len(cod_postal)
    if lcp == 8:
        return 'Argentina'
    elif lcp == 4:
        return 'Bolivia'
    elif lcp == 9:
        return 'Brasil'
    elif lcp == 7:
        return 'Chile'
    elif lcp == 6:
        return 'Paraguay'
    elif lcp == 5:
        return 'Uruguay'
    else:
        return 'Otro'

def determinar_provincia(cod_postal):
    if cod_postal != '' and cod_postal[0] == 'B':
        return 'Buenos Aires'
    return 'Otra'

def main():
    tratar_archivo = open('./tps/envios100HC.txt', 'rt')
    texto = tratar_archivo.readline()
    while True:
        linea = tratar_archivo.readline()
        if not linea:
            break
        cod_postal = linea[0:9].strip()
        direccion = linea[9:29].strip()
        tipo_envio = int(linea[29])
        forma_pago = int(linea[30])
        tipo_control_texto = detectar_tipo_control(texto)
        r1 = tipo_control_texto
        r2 = r3 = r4 = r5 = r6 = r7 = r10 = indice = 0
        r8 = r9 = r12 = ""
        r11 = 9999
        total_envios = 0
        total_envios_exterior = 0
        total_importe_buenos_aires = 0
        envios_buenos_aires = 0
        while indice < len(texto):
            nuevo_indice = obtener_indice(texto, indice)
            indice = nuevo_indice
            if linea == '':
                continue
            es_valido = validar_direccion(direccion, r1)
            precio = calcular_precio(tipo_envio, cod_postal)
            if forma_pago == 1:
                precio = precio * 0.9
            if tipo_control_texto == 'Hard Control':
                if es_valido:
                    r2 += 1
                    r4 += precio
                else:
                    r3 += 1
                if tipo_envio == 0:
                    r5 += 1
                elif tipo_envio == 1:
                    r6 += 1
                elif tipo_envio == 2:
                    r7 += 1
            elif tipo_control_texto == 'Soft Control':
                r2 += 1
                r3 = 0
                r4 += precio
                if tipo_envio == 0:
                    r5 += 1
                elif tipo_envio == 1:
                    r6 += 1
                elif tipo_envio == 2:
                    r7 += 1
            if total_envios == 0:
                r9 = cod_postal
                r10 = 1
            elif r9 == cod_postal:
                r10 += 1
            if determinar_pais(cod_postal) == 'Brasil' and precio < r11:
                r11 = precio
                r12 = cod_postal
            if determinar_provincia(cod_postal) == 'Buenos Aires':
                total_importe_buenos_aires += precio
                envios_buenos_aires += 1
            if determinar_pais(cod_postal) != 'Argentina':
                total_envios_exterior += 1
            total_envios += 1
        if r5 > r6 and r5 > r7:
            r8 = 'Carta Simple'
        elif r6 > r5 and r6 > r7:
            r8 = 'Carta Certificada'
        elif r7 > r5 and r7 > r6:
            r8 = 'Carta Expresa'
        else:
            if r5 == r6 and r5 == r7:
                r8 = 'Carta Simple'
            elif r5 == r6:
                r8 = 'Carta Simple'
            elif r5 == r7:
                r8 = 'Carta Simple'
            elif r6 == r7:
                r8 = 'Carta Certificada'
        if total_envios > 0:
            r13 = (total_envios_exterior * 100) // total_envios
        else:
            r13 = 0
        if envios_buenos_aires > 0:
            r14 = total_importe_buenos_aires // envios_buenos_aires
        else:
            r14 = 0
    # print('(r1) - Tipo de control de direcciones:', r1)
    # print('(r2) - Cantidad de envios con direccion valida:', r2)
    # print('(r3) - Cantidad de envíos con direccion no valida:', r3)
    # print('(r4) - Total acumulado de importes finales:', r4)
    # print('(r5) - Cantidad de cartas simples:', r5)
    # print('(r6) - Cantidad de cartas certificadas:', r6)
    # print('(r7) - Cantidad de cartas expresas:', r7)
    # print('(r8) - Tipo de carta con mayor cantidad de envios:', r8)
    # print('(r9) - Codigo postal del primer envio del archivo:', r9)
    # print('(r10) - Cantidad de veces que entro ese primero:', r10)
    # print('(r11) - Importe menor pagado por envios a Brasil:', r11)
    # print('(r12) - Codigo postal del envio a Brasil con importe menor:', r12)
    # print('(r13) - Porcentaje de envíos al exterior sobre el total:', r13)
    # print('(r14) - Importe final promedio de los envíos a Buenos Aires:', r14)
    # tratar_archivo.close()

    print(f'Tipo de control: {r1}')

main()
