
def montos(curso1, curso2, curso3):

    monto1 = curso1 * 1360
    monto2 = curso2 * 1360
    monto3 = curso3 * 1360

    if curso1 > 40:
        monto1 *= 0.95
    if curso2 > 40:
        monto2 *= 0.95
    if curso3 > 40:
        monto3 *= 0.95

    return monto1, monto2, monto3


def mayorCurso(curso1, monto1, curso2, monto2, curso3, monto3):
    if curso1 > curso2 and curso1 > curso3:
        mayor = curso1
        monto_mayor = monto1
    else:
        if curso2 > curso3:
            mayor = curso2
            monto_mayor = monto2
        else:
            mayor = curso3
            monto_mayor = monto3

    return mayor, monto_mayor


def porcentaje(m1, m2, m3, mayor):
    monto_total = m1 + m2 + m3
    if monto_total > 0:
        porcentaje_monto_mayor = round((mayor * 100) / monto_total, 2)
    else:
        porcentaje_monto_mayor = 0
    return porcentaje_monto_mayor



def test():
    curso_1 = int(input('Ingrese la cant de alumnos del curso 1: '))
    curso_2 = int(input('Ingrese la cant de alumnos del curso 2: '))
    curso_3 = int(input('Ingrese la cant de alumnos del curso 3: '))

    monto1, monto2, monto3 = montos(curso_1, curso_2, curso_3)

    print('-'*90)
    print('Los montos son: ')
    print(f'El monto del curso 1 es: ${monto1}')
    print(f'El monto del curso 2 es: ${monto2}')
    print(f'El monto del curso 3 es: ${monto3}')
    print('-'*90)

    mayor_curso, mayor_monto_generado = mayorCurso(curso_1, monto1, curso_2, monto2, curso_3, monto3)

    print(f'El mayor curso tiene: {mayor_curso}')
    print(f'El monto generado por dicho curso es de: ${mayor_monto_generado}')
    print('-'*90)

    porcentaje_generado_mayor_curso = porcentaje(monto1, monto2, monto3, mayor_monto_generado)

    print(f'El porcentaje generado, por el ingreso del mayor curso, sobre el total de ingresos es: {porcentaje_generado_mayor_curso}%')
    print('-'*90)





test()

