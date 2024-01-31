nombre_empleado = input('Ingrese el nombre del salario actual del empleado: ')
area_empleado = input('Ingrese el area a la que pertenece dicho empleado: ')
salario_actual_empleado = float(input('ingrese el sueldo actual del empleado: '))

incremento = salario_actual_empleado * 0.8
descuento = salario_actual_empleado * 0.025
nuevo_salario_empleado = salario_actual_empleado + incremento - descuento

print(f'Nombre empleado: {nombre_empleado}, \t Nuevo sueldo: {nuevo_salario_empleado}  ' )
print(f'Area funcional: {area_empleado}')
print(f'Salario actual: {salario_actual_empleado}')
