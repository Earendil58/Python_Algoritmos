def promedio_anual(lluvias):
    lluvias_anuales = lluvias
    acumulado_lluvias_anuales = 0

    for lluvia_mensual in lluvias_anuales:
        acumulado_lluvias_anuales += lluvia_mensual

    promedio_anual_lluvias = round(acumulado_lluvias_anuales / 12,2)

    return promedio_anual_lluvias


def promedio_lluvias_trimestre(lluvias, trimestre):
    trimestre_empieza = None
    trimestre_termina = None
    acumulador_lluvias_trimestrales = 0

    if trimestre == 1:
        trimestre_empieza = 0
        trimestre_termina = 3
    elif trimestre == 2:
        trimestre_empieza = 3
        trimestre_termina = 6
    elif trimestre == 3:
        trimestre_empieza = 6
        trimestre_termina = 9
    elif trimestre == 4:
        trimestre_empieza = 9
        trimestre_termina = 12

    lluvia_trimestre_elegido = lluvias[trimestre_empieza:trimestre_termina]


    for lluvia in lluvia_trimestre_elegido:
        acumulador_lluvias_trimestrales += lluvia

    promedio_de_lluvias_trimestre_elegido = round(acumulador_lluvias_trimestrales / 3, 2)

    return promedio_de_lluvias_trimestre_elegido


def mes_mas_seco(lluvias):
    menor = 0

    for lluvia in lluvias:
        if menor == 0:
            menor = lluvia
        else:
            if lluvia < menor:
                menor = lluvia

    return menor


def test():
    lluvias_registradas = []

    for mes in range(1,13):
        mes_lluvia = int(input(f'Ingrese las lluvias registradas para el mes {mes}: '))
        lluvias_registradas.append(mes_lluvia)

    promedio_anual_lluvias = promedio_anual(lluvias_registradas)

    print(f'El promedio anual de lluvias es de: {promedio_anual_lluvias} mm')

    trimestre_elegido = int(input('Ingrese el trimestre elegido para validar el promedio (1,2,3,4): '))

    promedio_lluvias_por_trimestre = promedio_lluvias_trimestre(lluvias_registradas, trimestre_elegido)

    print(f'El promedio de lluvias, en el trimestre: {trimestre_elegido} fue de: {promedio_lluvias_por_trimestre} mm')

    mes_menor_lluvia = mes_mas_seco(lluvias_registradas)

    print(f'El mes de menor lluvias, registró: {mes_menor_lluvia} mm')


if __name__ == '__main__':
    test()
