#Ingreso de datos

cant_total_pers = int(input('Ingrese la cantidad total de personas enfermas: '))
cant_local_pers = int(input('Ingrese cantidad total de personas enfermas en la ciudad: '))

#Operación

porcentaje = (cant_local_pers / cant_total_pers) * 100

print('El porcentaje es',porcentaje,'%')
