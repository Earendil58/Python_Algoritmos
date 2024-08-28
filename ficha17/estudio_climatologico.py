
def cargar_datos():
    n = int(input("Ingrese la cantidad de muestras a registrar: "))
    temperaturas = [0.0] * n
    regiones = [0] * n
    dias = [0] * n
    for i in range(n):
        dia = int(input("Ingrese día: "))
        region = int(input("Ingrese región: "))
        temperatura = float(input("Ingrese temperatura: "))
        dias[i] = dia
        regiones[i] = region
        temperaturas[i] = temperatura
    return dias, regiones, temperaturas

def menu():
    print('-' * 90)
    print('Ingrese algunas de las siguientes opciones: ')
    print('1) Determinar el promedio general de temperatura')
    print('2) Dada una región, mostrar las temperaturas de la misma, ordenadas por dia, de menor a mayor')
    print('3) Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado')
    print('4) Determinar la cantidad de muestras por region (20 contadores)')
    opcion_elegida = int(input('Ingresa la opción elegida: '))
    print('-' * 90)

    return opcion_elegida

def promedio_gral_temperaturas(temperaturas):
    longitud_array_temperaturas = len(temperaturas)
    acumulador_temperaturas = None

    for temperatura in temperaturas:
        if acumulador_temperaturas is None:
            acumulador_temperaturas = temperatura
        else:
            acumulador_temperaturas += temperatura

    promedio_temperaturas = round(acumulador_temperaturas / longitud_array_temperaturas, 2)

    return promedio_temperaturas

def ordenar_temperaturas(temperaturas, dias,regiones):
    longitud_array = len(temperaturas)
    for i in range(longitud_array):
        for j in range(0, longitud_array - i - 1):
            if temperaturas[j] > temperaturas[j + 1]:
                temperaturas[j], temperaturas[j + 1] = temperaturas[j + 1], temperaturas[j]
                dias[i], dias[j + 1] = dias[j + 1], dias[j]
                regiones[j], regiones[j + 1] = regiones[j + 1], regiones[j]

    return temperaturas

def temperaturas_por_region(regiones, temperaturas, reg):
    longitud_array_regiones = len(regiones)
    temperas_de_region = []

    for region in range(longitud_array_regiones):
        if regiones[region] == reg:
            temperas_de_region.append(temperaturas[region])

    return temperas_de_region



def principal():
    dias, regiones, temperaturas = cargar_datos()
    opcion_elegida = menu()

    print(f'Las regiones mencionadas son: {regiones}')
    print(f'Las temperaturas mencionadas allí, son: {temperaturas}')
    print(f'Los días allí mencionados son: {dias}')

    if opcion_elegida == 1:
        promedios_de_temperaturas = promedio_gral_temperaturas(temperaturas)
        print(f'El promedio de las temperaturas registradas es: {promedios_de_temperaturas}')

    elif opcion_elegida == 2:
        temperaturas_ord_asc = ordenar_temperaturas(temperaturas,dias,regiones)
        print(f'Las temperaturas, ordenadas de manera ascendentes son: {temperaturas_ord_asc}')

        region_elegida_para_mostrar_temperaturas = int(input('Ingrese la región para evaluar sus temperaturas: '))
        temperaturas_por_regiones = temperaturas_por_region(regiones, temperaturas, region_elegida_para_mostrar_temperaturas)
        print(f'Las temperaturas de la region: {region_elegida_para_mostrar_temperaturas}, son: {temperaturas_por_regiones}')



if __name__ == '__main__':
    principal()


