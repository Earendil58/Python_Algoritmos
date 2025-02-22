def desgloce_temporal(centesimas):
    minutos = centesimas // (60 * 100)
    centesimas_restantes = centesimas % (60 * 100)
    segundos = centesimas_restantes // 100
    centesimas_finales = centesimas_restantes % 100

    return minutos, segundos, centesimas_finales


def main():
    #TIEMPOS EQUIPO GANADOR:

    espalda = (52 * 100) + 15  # Tiempo en centésimas
    pecho = (1 * 60 * 100) + (2 * 100) + 75  # 1 min, 2 seg, 75 centésimas
    mariposa = (59 * 100) + 80
    libre = (48 * 100) + 15

    tiempo_total_carrera = espalda + pecho + mariposa + libre

    minutos, segundos, centesimas = desgloce_temporal(tiempo_total_carrera)


    print(f'El tiempo total de carrera es: {minutos} minutos, {segundos} segundos y {centesimas} centésimas.')


if __name__ == "__main__":
    main()





