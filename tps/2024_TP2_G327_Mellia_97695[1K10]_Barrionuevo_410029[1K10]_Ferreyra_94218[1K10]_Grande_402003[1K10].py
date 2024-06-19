#ENTRADAS
tipo_control = primercod_pos = ""
direcciones_validas = direcciones_invalidas = acumulador_importe_final = carta_simple = carta_certificada = carta_expresa = 0

def obtener_tipo_control(linea):
    if "HC" in linea or "hc" in linea:
        tipo_control = "Hard Control"
    elif "SC" in linea or "sc":
        tipo_control = "Soft Control"
    return tipo_control


def linea_sin_saltos(linea):
    if linea[-1] == "\n":
        linea = linea[:-1]
    return linea


def extraer_datos(linea):
    cod = linea[0:9].strip()
    dir = linea[9:29].strip()
    tipo = int(linea[29])
    forma = int(linea[30])
    return cod, dir, tipo, forma


def controlar_direcciones(dir,tipo_control,cod_pos,tipo,forma):

    control = tipo_control
    direccion = dir

    informe_cod_pos = ()
    informe_tipo_de_envio = ()
    informe_forma_de_pago = ()

    tiene_dos_mayusculas_seguidas = boolEsDigito = False
    #Cadenas de Caracteres
    digitos = "0123456789"
    letras_con_acento_minusculas = "áéíóúñü"
    letras_con_acento_mayusculas = "ÁÉÍÓÚÑÜ"
    letras_sin_acento_minusculas = "abcdefghijklmnopqrstuvwxyz"
    letras_sin_acento_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caracteres = digitos+letras_con_acento_minusculas+letras_con_acento_mayusculas+letras_sin_acento_minusculas+letras_sin_acento_mayusculas+" ."
    mayusculas = letras_con_acento_mayusculas+letras_sin_acento_mayusculas
    anterior = " "
    direccion_len = len(direccion)

    contador = direccion_hc = direccion_sc = 0

    if control == "Hard Control":
        for car in direccion:
            if car != " " or car != ".":

                if car in digitos:
                    boolEsDigito = True
                elif car not in digitos and anterior not in digitos:
                    boolEsDigito = False

                if anterior in mayusculas and car in mayusculas:
                    tiene_dos_mayusculas_seguidas = True
                anterior = car

            if car in caracteres:
                contador += 1
        #Discriminar entre HC y SC
        if direccion_len == contador and tiene_dos_mayusculas_seguidas == False and boolEsDigito:
            #Guardar Datos del envio
            informe_cod_pos = (cod_pos)
            informe_tipo_de_envio = (tipo)
            informe_forma_de_pago = (forma)
            direccion_hc += 1
        else: direccion_sc += 1

        direcciones_validas = direccion_hc
        direcciones_invalidas = direccion_sc
    elif control == "Soft Control":

        direccion_sc += 1

        direcciones_validas = direccion_sc
        direcciones_invalidas = direccion_hc

        informe_cod_pos = (cod_pos)
        informe_tipo_de_envio = (tipo)
        informe_forma_de_pago = (forma)
    #Salidas
    return direcciones_validas,direcciones_invalidas,informe_cod_pos,informe_tipo_de_envio,informe_forma_de_pago
def acumulador_de_importes(cp,tipo,pago):

    cp_len = len(cp)

    total_envios_exterior = destino_BA = False

    destino = provincia = "Otro"
    #Int Enteros
    inicial = final = final_float = carta_simple = carta_certificada = carta_expresa = 0

    cp_arg = cp_len == 8 and cp[0] >= "A" and cp[0] <= "Z" and cp[0] != "O" and cp[0] != "l" and cp[0] != "I" and cp[1] >= "0" and cp[1] <= "9" and cp[2] >= "0" and cp[2] <= "9" and cp[3] >= "0" and cp[3] <= "9" and cp[4] >= "0" and cp[4] <= "9" and cp[5] >= "A" and cp[5] <= "Z" and cp[6] >= "A" and cp[6] <= "Z" and cp[7] >= "A" and cp[7] <= "Z"
    cp_bolivia = cp_len == 4 and cp[0] >= "0" and cp[0] <= "9" and cp[1] >= "0" and cp[1] <= "9" and cp[2] >= "0" and cp[2] <= "9" and cp[3] >= "0" and cp[3] <= "9"
    cp_brasil = cp_len == 9 and cp[0] >= "0" and cp[0] <= "9" and cp[1] >= "0" and cp[1] <= "9" and cp[2] >= "0" and cp[2] <= "9" and cp[3] >= "0" and cp[3] <= "9" and cp[4] >= "0" and cp[4] <= "9" and cp[5] == "-" and cp[6] >= "0" and cp[6] <= "9" and cp[7] >= "0" and cp[7] <= "9" and cp[8] >= "0" and cp[8] <= "9"
    cp_chile = cp_len == 7 and cp[0] >= "0" and cp[0] <= "9" and cp[1] >= "0" and cp[1] <= "9" and cp[2] >= "0" and cp[2] <= "9" and cp[3] >= "0" and cp[3] <= "9" and cp[4] >= "0" and cp[4] <= "9" and cp[5] >= "0" and cp[5] <= "9" and cp[6] >= "0" and cp[6] <= "9"
    cp_paraguay = cp_len == 6 and cp[0] >= "0" and cp[0] <= "9" and cp[1] >= "0" and cp[1] <= "9" and cp[2] >= "0" and cp[2] <= "9" and cp[3] >= "0" and cp[3] <= "9" and cp[4] >= "0" and cp[4] <= "9" and cp[5] >= "0" and cp[5] <= "9"
    cp_uruguay = cp_len == 5 and cp[0] >= "0" and cp[0] <= "9" and cp[1] >= "0" and cp[1] <= "9" and cp[2] >= "0" and cp[2] <= "9" and cp[3] >= "0" and cp[3] <= "9" and cp[4] >= "0" and cp[4] <= "9" 
    #Procesos
    #Determinar Pais
    if cp_arg:
        destino = "Argentina"
    elif cp_bolivia:
        destino = "Bolivia"
    elif cp_brasil:
        destino = "Brasil"
    elif cp_chile:
        destino = "Chile"
    elif cp_paraguay:
        destino = "Paraguay"
    elif cp_uruguay:
        destino = "Uruguay"
    else: destino = "Otro"

    if destino != "Argentina":
        total_envios_exterior = True

    if tipo == 0:
        carta_simple += 1
        inicial = 1100
    elif tipo == 1:
        carta_simple += 1
        inicial = 1800
    elif tipo == 2:
        carta_simple += 1
        inicial = 2450
    elif tipo == 3:
        carta_certificada += 1
        inicial = 8300
    elif tipo == 4:
        carta_certificada += 1
        inicial = 10900
    elif tipo == 5:
        carta_expresa += 1
        inicial = 14300
    elif tipo == 6:
        carta_expresa += 1
        inicial = 17900

    if destino == "Argentina":
        if cp[0] == 'B':
            provincia = "Provincia de Buenos Aires"

    elif destino == "Bolivia" or destino == "Paraguay" or destino == "Uruguay" or destino == "Chile" or destino == "Brasil":

        if destino == "Uruguay" and cp[0] == "1":
            aumentar = inicial * 0.20
            inicial += aumentar
        elif destino == "Uruguay" and cp[0] != "1":
            aumentar = inicial * 0.25
            inicial += aumentar             

        elif destino == "Bolivia" or destino == "Paraguay":
            aumentar = inicial * 0.20
            inicial += aumentar

        elif destino == "Chile":
            aumentar = inicial * 0.25
            inicial += aumentar

        elif destino == "Brasil" and cp[0] == "8" or cp[0] == "9":
            aumentar = inicial * 0.20
            inicial += aumentar 
        elif destino == "Brasil" and cp[0] == "0" or cp[0] == "1" or cp[0] == "2" or cp[0] == "3":
            aumentar = inicial * 0.25
            inicial += aumentar
        elif destino == "Brasil" and cp[0] == "4" or cp[0] == "5" or cp[0] == "6" or cp[0] == "7":
            aumentar = inicial * 0.30
            inicial += aumentar
    else:
        aumentar = inicial * 0.50
        inicial += aumentar

    if pago == 1:
        descuento  = inicial * 0.10
        final_float = inicial - descuento
        final = final_float
    elif pago == 2:
        final = inicial

    return final,carta_simple,carta_certificada,carta_expresa,total_envios_exterior,provincia
def calcular_mayor_entre_cartas(ccs,ccc,cce):
    if ccs >= ccc and ccs >= cce:
        mayor = "Carta Simple"
    elif ccc >= ccs and ccc >= cce:
        mayor = "Carta Certificada"
    else:
        mayor = "Carta Expresa"
    return mayor
def calcular_porcentaje_promedio(total_envios,ctotal_envios_exterior,monto_BA,cenvios_BA):

    if total_envios > 0: porcentaje = (ctotal_envios_exterior * 100) / total_envios
    else: porcentaje = 0

    if cenvios_BA > 0:
        promedio = monto_BA / cenvios_BA
    else: promedio = 0
    porcentaje = int(porcentaje)
    promedio = int(promedio)
    return porcentaje,promedio
def identificar_cp_brasil(cp):

    cp_len = len(cp)
    destino = ""
    cp_brasil = cp_len == 9 and cp[0] >= "0" and cp[0] <= "9" and cp[1] >= "0" and cp[1] <= "9" and cp[2] >= "0" and cp[2] <= "9" and cp[3] >= "0" and cp[3] <= "9" and cp[4] >= "0" and cp[4] <= "9" and cp[5] == "-" and cp[6] >= "0" and cp[6] <= "9" and cp[7] >= "0" and cp[7] <= "9" and cp[8] >= "0" and cp[8] <= "9"
    if cp_brasil:
        destino = "Brasil"
    return destino

def principal(tipo_control,direcciones_validas,direcciones_invalidas,acumulador_importe_final,carta_simple,carta_certificada,carta_expresa):
    #Entradas
    #Abrimos el Archivo, leemos la primera linea y obtenemos el tipo de control
    archivo = open("envios25.txt", "rt", encoding="utf-8")
    linea = archivo.readline()
    tipo_control = obtener_tipo_control(linea)
    #Cadenas
    mayor = primercod_pos = cp_brasil = destino_brasil = ""
    #Contadores,Acumuladores,etc
    cont_direcciones_validas = cont_direcciones_invalidas = ccs = ccc = cce = cont_primercod_pos = total_envios = ctotal_envios_exterior = cenvios_BA = acumulador_importe_final = monto_BA = 0
    repeticiones_while = menor = None
    #Bool
    total_envios_exterior = False
    #Leemos la siguiente línea después de obtener el tipo de control
    linea = archivo.readline()
    #Procesos
    while linea != "":
        linea = linea_sin_saltos(linea)
        #Extraemos los datos de la linea
        cod_pos, dir, tipo, forma = extraer_datos(linea)
        #Identificamos el primer codigo postal
        if repeticiones_while == None:
            repeticiones_while = 0
            primercod_pos = cod_pos
        if cod_pos == primercod_pos:
            cont_primercod_pos += 1
        #Controlamos las direcciones
        direcciones_validas,direcciones_invalidas,informe_cod_pos,informe_tipo_de_envio,informe_forma_de_pago = controlar_direcciones(dir,tipo_control,cod_pos,tipo,forma)
        cont_direcciones_validas += direcciones_validas
        cont_direcciones_invalidas += direcciones_invalidas
        #Acumulador de importe final $$$
        if informe_cod_pos != () and informe_forma_de_pago != () and informe_tipo_de_envio != (): 
            importe,carta_simple,carta_certificada,carta_expresa,total_envios_exterior,envios_BA = acumulador_de_importes(informe_cod_pos,informe_tipo_de_envio,informe_forma_de_pago)
            if envios_BA == "Provincia de Buenos Aires": 
                monto_BA += importe
                cenvios_BA += 1
            acumulador_importe_final += importe
            ccs += carta_simple
            ccc += carta_certificada
            cce += carta_expresa
        #Obtener el menor de los destinos de brasil
        destino_brasil = identificar_cp_brasil(cod_pos)
        if destino_brasil == "Brasil":
            if menor is None or importe < menor:
                menor = importe
                cp_brasil = cod_pos
        #Contar envios al exterior y envios totales
        total_envios += 1
        if total_envios_exterior: ctotal_envios_exterior += 1
        linea = archivo.readline()
    #Cerramos el arhivo para ahorrar memoria
    archivo.close()
    #Calcular mayor entre cartas
    mayor = calcular_mayor_entre_cartas(ccs,ccc,cce)
    #Calcular el porcentaje que representa la cantidad total de envíos al exterior sobre la cantidad total de envíos Y Calcular Promedio de envios a Provincia de Buenos Aires
    porcentaje,promedio = calcular_porcentaje_promedio(total_envios,ctotal_envios_exterior,monto_BA,cenvios_BA)
    #Salidas
    return tipo_control,cont_direcciones_validas,cont_direcciones_invalidas,acumulador_importe_final,ccs,ccc,cce,mayor,primercod_pos,cont_primercod_pos,menor,cp_brasil,porcentaje,promedio

tipo_control,direcciones_validas,direcciones_invalidas,acumulador_importe_final,carta_simple,carta_certificada,carta_expresa,mayor,primercod_pos,cont_primercod_pos,menor,cp_brasil,porcentaje,promedio = principal(tipo_control,direcciones_validas,direcciones_invalidas,acumulador_importe_final,carta_simple,carta_certificada,carta_expresa)
#SALIDAS
print(' (r1) - Tipo de control de direcciones:', tipo_control)
print(' (r2) - Cantidad de envios con direccion valida:', direcciones_validas)
print(' (r3) - Cantidad de envios con direccion no valida:', direcciones_invalidas)
print(' (r4) - Total acumulado de importes finales:', acumulador_importe_final)
print(' (r5) - Cantidad de cartas simples:', carta_simple)
print(' (r6) - Cantidad de cartas certificadas:', carta_certificada)
print(' (r7) - Cantidad de cartas expresas:', carta_expresa)
print(' (r8) - Tipo de carta con mayor cantidad de envios:', mayor)
print(' (r9) - Codigo postal del primer envio del archivo:', primercod_pos)
print('(r10) - Cantidad de veces que entro ese primero:', cont_primercod_pos)
print('(r11) - Importe menor pagado por envios a Brasil:', menor)
print('(r12) - Codigo postal del envio a Brasil con importe menor:', cp_brasil)
print('(r13) - Porcentaje de envios al exterior sobre el total:', porcentaje,"%")
print('(r14) - Importe final promedio de los envios a Buenos Aires:', promedio)
