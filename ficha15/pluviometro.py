def promedio_anual(lluvias):
    lluvias_anuales = lluvias
    acumulado_lluvias_anuales = 0

    for lluvia_mensual in lluvias_anuales:
        acumulado_lluvias_anuales += lluvia_mensual

    promedio_anual_lluvias = round(acumulado_lluvias_anuales / 12,2)

    return promedio_anual_lluvias



def test():
    lluvias_registradas = []

    for mes in range(1,13):
        mes_lluvia = int(input(f'Ingrese las lluvias registradas para el mes {mes}: '))
        lluvias_registradas.append(mes_lluvia)


    promedio_anual_lluvias = promedio_anual(lluvias_registradas)

    print(promedio_anual_lluvias)


if __name__ == '__main__':
    test()
