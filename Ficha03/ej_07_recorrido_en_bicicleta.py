def validador_numerico(valor):
    while True:
        try:
            if valor > 0:
                return valor
            else:
                print('El valor debe ser un número positivo')
        except ValueError:
            print('Por favor ingrese un monto válido')

def convertidor_de_metros_a_kilometros(metros):
    metros_a_kilometros = metros / 1000
    return metros_a_kilometros

def calcular_porcentaje_viaje(metros_recorridos_hasta_accidente, distancia_total_viaje_pretendido):
    porcentaje = (metros_recorridos_hasta_accidente * 100) / distancia_total_viaje_pretendido
    porcentaje_redondeado = round(porcentaje,2)
    return porcentaje_redondeado


def main():
    DIST_TOTAL_VIAJE_EN_METROS = 3641.3 * 1000

    dist_en_metros_de_accidente = validador_numerico(float(input('Por favor, ingrese los metros a los que sufrió el accidente: ')))
    distancia_en_km_hasta_accidente = convertidor_de_metros_a_kilometros(dist_en_metros_de_accidente)
    porcentaje_del_viaje = calcular_porcentaje_viaje(dist_en_metros_de_accidente, DIST_TOTAL_VIAJE_EN_METROS)

    print('Análisis del recorrido:')
    print(f'El viajero sufrió un accidente a los {dist_en_metros_de_accidente} metros, de la partida')
    print(f'La distancia total recorrida, hasta el accidente, fue de: {distancia_en_km_hasta_accidente} kms')
    print(f'El porcentaje del viaje, recorrido, hasta el accidente, es de: {porcentaje_del_viaje}%')



if __name__ == '__main__':
    main()
