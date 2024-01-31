def cursoMasNumeroso(curso1, curso2, curso3):
    if curso1 > curso2 and curso1 > curso3:
        mayor = curso1
    else:
        if curso2 > curso3:
            mayor = curso2
        else:
            mayor = curso3

    return mayor


def aplicaDescuento(numero):
    PRECIO = 1360
    if numero > 40:
        precio_total = numero * (PRECIO * 0.95)
    else:
        precio_total = numero * PRECIO

    return precio_total

def precioPorAlumno(numerosAlumnos):
    precio_viaje = aplicaDescuento(numerosAlumnos)
    precio_por_alumno = precio_viaje / numerosAlumnos

    return precio_por_alumno



def analizarViaje(curso1, curso2, curso3):
    cursoMayor = cursoMasNumeroso(curso1, curso2, curso3)
    paga_cada_curso = [aplicaDescuento(curso1), aplicaDescuento(curso2), aplicaDescuento(curso3)]
    precio_individual_por_curso = [precioPorAlumno(curso1), precioPorAlumno(curso2), precioPorAlumno(curso3)]

    print(f'El curso más númeroso es: {cursoMayor}')
    print(f'Los cursos pagaran lo siguiente:')
    print(f'El curso 1: ${paga_cada_curso[0]}, el precio por alumno es: ${precio_individual_por_curso[0]}')
    print(f'El curso 2: ${paga_cada_curso[1]}, el precio por alumno es: ${precio_individual_por_curso[1]}')
    print(f'El curso 3: ${paga_cada_curso[2]}, el precio por alumno es: ${precio_individual_por_curso[2]}')


analizarViaje(40, 38, 42)
