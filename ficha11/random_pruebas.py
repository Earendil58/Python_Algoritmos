def costo_por_curso(*args):
    ganancia_empresa = 0

    for curso in range(len(args)):
        tamaño_curso = args[curso]

        if tamaño_curso <= 40:
            costo_curso = tamaño_curso * 1360
        else:
            costo_curso = (tamaño_curso * 1360) * 0.95

        ganancia_empresa += costo_curso



    return ganancia_empresa


def curso_mas_numeroso(*args):
    curso_mayor = float('-inf')
    indice_curso_mayor = None

    for i in range(len(args)):
        tamaño_curso = args[i]
        print(f'El curso {i + 1} tiene: {tamaño_curso} alumnos')

        if tamaño_curso > curso_mayor:
            curso_mayor = tamaño_curso
            indice_curso_mayor = i + 1


    return curso_mayor


def analizar_viaje(*args):
    curso_mayor = curso_mas_numeroso(*args)
    costo_por_cada_curso = costo_por_curso(*args)

    print("Total de alumnos en el curso más numeroso:", curso_mayor)
    print("Ganancia total de la empresa:", costo_por_cada_curso)

analizar_viaje(40, 12, 55, 101, 12)
