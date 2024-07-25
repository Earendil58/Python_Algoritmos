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

    print(lluvia_trimestre_elegido)



def test():
    lluvias_registradas = []

    for mes in range(1,13):
        mes_lluvia = int(input(f'Ingrese las lluvias registradas para el mes {mes}: '))
        lluvias_registradas.append(mes_lluvia)


    promedio_anual_lluvias = promedio_anual(lluvias_registradas)

    print(promedio_anual_lluvias)

    trimestre_elegido = int(input('Ingrese el trimestre elegido para validar el promedio (1,2,3,4): '))

    lluvias_por_trimestre = promedio_lluvias_trimestre(lluvias_registradas, trimestre_elegido)

    print(lluvias_por_trimestre)



if __name__ == '__main__':
    test()
