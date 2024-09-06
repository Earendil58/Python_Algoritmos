#ENTRADAS
tipo_control = primercod_pos = ""
direcciones_validas = direcciones_invalidas = acumulador_importe_final = carta_simple = carta_certificada = carta_expresa = 0

def obtener_tipo_control(linea):
    if "HC" in linea or "hc" in linea:
        return "Hard Control"
    elif "SC" in linea or "sc" in linea:
        return "Soft Control"
    return ""

def linea_sin_saltos(linea):
    return linea.rstrip('\n')

def extraer_datos(linea):
    return linea[0:9].strip(), linea[9:29].strip(), int(linea[29]), int(linea[30])

def controlar_direcciones(dir, tipo_control, cod_pos, tipo, forma):
    control = tipo_control
    digitos = "0123456789"
    letras_con_acento_minusculas = "áéíóúñü"
    letras_con_acento_mayusculas = "ÁÉÍÓÚÑÜ"
    letras_sin_acento_minusculas = "abcdefghijklmnopqrstuvwxyz"
    letras_sin_acento_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caracteres = digitos + letras_con_acento_minusculas + letras_con_acento_mayusculas + letras_sin_acento_minusculas + letras_sin_acento_mayusculas + " ."
    mayusculas = letras_con_acento_mayusculas + letras_sin_acento_mayusculas

    tiene_dos_mayusculas_seguidas = False
    boolEsDigito = False
    contador = 0
    anterior = " "

    for car in dir:
        if car in caracteres:
            contador += 1
            if car in digitos:
                boolEsDigito = True
            elif car in mayusculas and anterior in mayusculas:
                tiene_dos_mayusculas_seguidas = True
            anterior = car

    if control == "Hard Control":
        if len(dir) == contador and not tiene_dos_mayusculas_seguidas and boolEsDigito:
            return 1, 0, cod_pos, tipo, forma
        else:
            return 0, 1, cod_pos, tipo, forma
    elif control == "Soft Control":
        return 1, 0, cod_pos, tipo, forma

    return 0, 1, (), (), ()

def acumulador_de_importes(cp, tipo, pago):
    inicial = 0
    destino = "Otro"
    destino_BA = False
    cp_len = len(cp)

    if cp_len == 8 and cp[0].isalpha() and cp[1:5].isdigit() and cp[5:].isalpha():
        destino = "Argentina"
    elif cp_len == 4 and cp.isdigit():
        destino = "Bolivia"
    elif cp_len == 9 and cp[:5].isdigit() and cp[6:].isdigit() and cp[5] == "-":
        destino = "Brasil"
    elif cp_len == 7 and cp.isdigit():
        destino = "Chile"
    elif cp_len == 6 and cp.isdigit():
        destino = "Paraguay"
    elif cp_len == 5 and cp.isdigit():
        destino = "Uruguay"

    if tipo == 0:
        inicial = 1100
    elif tipo == 1:
        inicial = 1800
    elif tipo == 2:
        inicial = 2450
    elif tipo == 3:
        inicial = 8300
    elif tipo == 4:
        inicial = 10900
    elif tipo == 5:
        inicial = 14300
    elif tipo == 6:
        inicial = 17900

    if destino == "Argentina" and cp[0] == 'B':
        destino_BA = True
    else:
        aumentos = {
            "Uruguay": 0.20 if cp[0] == "1" else 0.25,
            "Bolivia": 0.20,
            "Paraguay": 0.20,
            "Chile": 0.25,
            "Brasil": 0.30 if cp[0] in "4567" else 0.25 if cp[0] in "0123" else 0.20
        }
        inicial += inicial * aumentos.get(destino, 0.50)

    if pago == 1:
        inicial -= inicial * 0.10

    carta_simple = carta_certificada = carta_expresa = 0
    if tipo in [0, 1, 2]:
        carta_simple = 1
    elif tipo in [3, 4]:
        carta_certificada = 1
    elif tipo in [5, 6]:
        carta_expresa = 1

    return inicial, carta_simple, carta_certificada, carta_expresa, destino != "Argentina", "Provincia de Buenos Aires" if destino_BA else "Otro"

def calcular_mayor_entre_cartas(ccs, ccc, cce):
    if ccs >= ccc and ccs >= cce:
        return "Carta Simple"
    elif ccc >= ccs and ccc >= cce:
        return "Carta Certificada"
    else:
        return "Carta Expresa"

def calcular_porcentaje_promedio(total_envios, ctotal_envios_exterior, monto_BA, cenvios_BA):
    porcentaje = (ctotal_envios_exterior * 100) // total_envios if total_envios else 0
    promedio = monto_BA // cenvios_BA if cenvios_BA else 0
    return porcentaje, promedio

def identificar_cp_brasil(cp):
    return "Brasil" if len(cp) == 9 and cp[:5].isdigit() and cp[5] == "-" and cp[6:].isdigit() else ""

def principal(tipo_control, direcciones_validas, direcciones_invalidas, acumulador_importe_final, carta_simple, carta_certificada, carta_expresa):
    with open("envios100HC.txt", "rt", encoding="utf-8") as archivo:
        linea = archivo.readline()
        tipo_control = obtener_tipo_control(linea)
        linea = archivo.readline()

        primercod_pos = cod_pos = ""
        cont_primercod_pos = total_envios = ctotal_envios_exterior = cenvios_BA = 0
        monto_BA = 0
        menor = None
        cp_brasil = ""

        while linea:
            linea = linea_sin_saltos(linea)
            cod_pos, dir, tipo, forma = extraer_datos(linea)

            if primercod_pos == "":
                primercod_pos = cod_pos
            if cod_pos == primercod_pos:
                cont_primercod_pos += 1

            dir_valida, dir_invalida, cod_pos, tipo, forma = controlar_direcciones(dir, tipo_control, cod_pos, tipo, forma)
            direcciones_validas += dir_valida
            direcciones_invalidas += dir_invalida

            if cod_pos:
                importe, c_simple, c_cert, c_expr, ext, prov = acumulador_de_importes(cod_pos, tipo, forma)
                if prov == "Provincia de Buenos Aires":
                    monto_BA += importe
                    cenvios_BA += 1
                acumulador_importe_final += importe
                carta_simple += c_simple
                carta_certificada += c_cert
                carta_expresa += c_expr

                if identificar_cp_brasil(cod_pos) == "Brasil" and (menor is None or importe < menor):
                    menor = importe
                    cp_brasil = cod_pos

                total_envios += 1
                if ext:
                    ctotal_envios_exterior += 1

            linea = archivo.readline()

    mayor = calcular_mayor_entre_cartas(carta_simple, carta_certificada, carta_expresa)
    porcentaje, promedio = calcular_porcentaje_promedio(total_envios, ctotal_envios_exterior, monto_BA, cenvios_BA)

    return tipo_control, direcciones_validas, direcciones_invalidas, acumulador_importe_final, carta_simple, carta_certificada, carta_expresa, mayor, primercod_pos, cont_primercod_pos, menor, cp_brasil, porcentaje, promedio

tipo_control, direcciones_validas, direcciones_invalidas, acumulador_importe_final, carta_simple, carta_certificada, carta_expresa, mayor, primercod_pos, cont_primercod_pos, menor, cp_brasil, porcentaje, promedio = principal(tipo_control, direcciones_validas, direcciones_invalidas, acumulador_importe_final, carta_simple, carta_certificada, carta_expresa)
#SALIDAS
print(' (r1) - Tipo de control de direcciones:', tipo_control)
print(' (r2) - Cantidad de envios con direccion valida:', direcciones_validas)
print(' (r3) - Cantidad de envios con direccion no valida:', direcciones_invalidas)
print(' (r4) - Total acumulado de importes finales:', acumulador_importe_final)
print(' (r5) - Tipo de carta con mayor cantidad de envios:', mayor)
print(' (r6) - Codigo Postal de la direccion del primer envio:', primercod_pos)
print(' (r7) - Cantidad de envios realizados al primer Codigo Postal:', cont_primercod_pos)
print(' (r8) - El menor importe final de envios a Brasil:', menor)
print(' (r9) - El Codigo Postal de la direccion con el menor importe de envio a Brasil:', cp_brasil)
print(' (r10) - Porcentaje de envios al exterior:', porcentaje)
print(' (r11) - Promedio de importes finales para la Provincia de Buenos Aires:', promedio)
