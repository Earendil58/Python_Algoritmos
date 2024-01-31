def promedio(cantPregRealizadas,cantPregAcertadas):
    promedio = round((cantPregAcertadas * 100) / cantPregRealizadas, 2)
    return promedio


def calificacionPostulante(nombrePostulante, cantPregRealizadas,cantPregAcertadas):

    promedio_postulante = promedio(cantPregRealizadas,cantPregAcertadas)

    if promedio_postulante >= 90:
        nivel = 'superior'

    elif 75<= promedio_postulante < 90:
        nivel = 'Medio'

    elif 50<= promedio_postulante < 75:
        nivel = 'Regular'

    elif promedio_postulante < 50:
        nivel = 'Fuera de nivel'


    print(f'El nivel del cantidato: {nombrePostulante} fue de: {promedio_postulante}%, su nivel es: {nivel}')



def test(cantPostulantes):
    promedios_candidatos = []
    mejor_promedio = None
    mejor_promedio_nombre = ''
    for i in range(cantPostulantes):
        nombre = input('Ingrese el nombre del postulante: ')
        cant_preguntas = int(input('Ingrese la cantidad de preguntas realizadas: '))
        cant_acertadas = int(input('Ingrese la cant de preguntas acertadas: '))

        postulante_entrevista = calificacionPostulante(nombre, cant_preguntas, cant_acertadas)
        print(postulante_entrevista)

        promedio_individual = promedio(cant_preguntas, cant_acertadas)

        if i == 0:
            mejor_promedio = promedio_individual
            mejor_promedio_nombre = nombre

        else:
            if promedio_individual > mejor_promedio:
                mejor_promedio = promedio_individual
                mejor_promedio_nombre = nombre


        promedios_candidatos.append(promedio_individual)

    print(f'Los promedios de los candidatos fueron: {promedios_candidatos}')
    print(f'El mejor promedio fue: {mejor_promedio}%, que pertenece a: {mejor_promedio_nombre}')










test(3)



