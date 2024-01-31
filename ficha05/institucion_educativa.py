print('Por favor ingrese la información de cada grado: ')

print('Primer grado a ingresar: ')

print('-' * 40)

grado_uno = input('Ingrese la identificacion del grado uno: ')
cant_ninos_uno = int(input('Ingrese la cant de niños del grado uno: '))
cant_ninas_uno = int(input('Ingrese la cant de niñas del grado uno: '))
cupo_max_uno = int(input('Ingrese el cupo max del grado uno: '))

print('-' * 40)

print('Segundo grado a ingresar: ')

print('-' * 40)

grado_dos = input('Ingrese la identificacion del grado dos: ')
cant_ninos_dos = int(input('Ingrese la cant de niños del grado dos: '))
cant_ninas_dos = int(input('Ingrese la cant de niñas del grado dos: '))
cupo_max_dos = int(input('Ingrese el cupo max del grado dos: '))

print('-' * 40)

print('Tercer grado a ingresar: ')

print('-' * 40)

grado_tres = input('Ingrese la identificacion del grado tres: ')
cant_ninos_tres = int(input('Ingrese la cant de niños del grado tres: '))
cant_ninas_tres = int(input('Ingrese la cant de niñas del grado tres: '))
cupo_max_tres = int(input('Ingrese el cupo max del grado tres: '))

print('-' * 40)

menor_cant_ninos_curso = ''


#PROBLEMA A)

if cant_ninos_uno < cant_ninos_dos and cant_ninos_uno < cant_ninos_tres:
    menor_cant_ninos_curso = cant_ninos_uno

elif cant_ninos_dos < cant_ninos_uno and cant_ninos_dos < cant_ninos_tres:
    menor_cant_ninos_curso = cant_ninos_dos

else:
    menor_cant_ninos_curso = cant_ninos_tres


#PROBLEMA B) Y C)

total_alumnos_grado_uno = cant_ninos_uno + cant_ninas_uno
porcentaje_ninos_grado_uno = round(((cant_ninos_uno * 100) / total_alumnos_grado_uno), 2)
porcentaje_ninas_grado_uno = round(((cant_ninas_uno * 100) / total_alumnos_grado_uno), 2)

print(f'El porcentaje de niños del grado uno es: {porcentaje_ninos_grado_uno}% y el de niñas es {porcentaje_ninas_grado_uno}%')


total_alumnos_grado_dos = cant_ninos_dos + cant_ninas_dos
porcentaje_ninos_grado_dos = round(((cant_ninos_dos * 100) / total_alumnos_grado_dos), 2)
porcentaje_ninas_grado_dos = round(((cant_ninas_dos * 100) / total_alumnos_grado_dos), 2)

print(f'El porcentaje de niños del grado dos es: {porcentaje_ninos_grado_dos}% y el de niñas es {porcentaje_ninas_grado_dos}%')

total_alumnos_grado_tres = cant_ninos_tres + cant_ninas_tres
porcentaje_ninos_grado_tres = round(((cant_ninos_tres * 100) / total_alumnos_grado_tres), 2)
porcentaje_ninas_grado_tres = round(((cant_ninas_tres * 100) / total_alumnos_grado_tres), 2)

print(f'El porcentaje de niños del grado tres es: {porcentaje_ninos_grado_tres}% y el de niñas es {porcentaje_ninas_grado_tres}%')

#PROBLEMA D)

promedio_gral_alumnos = round(((total_alumnos_grado_uno + total_alumnos_grado_dos + total_alumnos_grado_tres) / 3), 2)
print(f'El promedio gral de alumnos es de: {promedio_gral_alumnos} alumnos')

#PROBLEMA E)

if  total_alumnos_grado_uno > cupo_max_uno or total_alumnos_grado_dos > cupo_max_dos or total_alumnos_grado_tres > cupo_max_tres:
    print(f'Alguno de los grados mencionados supera el máximo permitido de alumnos')
