tiempo_natacion = input('Ingrese el tiempo en formato mm:ss para la natacion: ')
tiempo_ciclismo = input('Ingrese el tiempo en formato mm:ss para el ciclismo: ')
tiempo_pedestre = input('Ingrese el tiempo en formato mm:ss para el pedestre: ')


#HORA NATACION A SEGUNDOS

tiempo_natacion_hora_a_entero = tiempo_natacion[0] + tiempo_natacion[1]
tiempo_natacion_hora_a_entero = int(tiempo_natacion_hora_a_entero)
tiempo_natacion_hora_a_entero_a_segundo = tiempo_natacion_hora_a_entero * 60

print('tiempo natancion, de horas a entero',tiempo_natacion_hora_a_entero)

#SEGUNDOS NATACION A ENTEROS

tiempo_natacion_segundos_a_entero = tiempo_natacion[-2] + tiempo_natacion[-1]
tiempo_natacion_segundos_a_entero = int(tiempo_natacion_segundos_a_entero)

print('tiempo natacion, de segundos a entero',tiempo_natacion_segundos_a_entero)

#TIEMPO TOTAL NATACION EN SEGUNDOS

tiempo_natacion_total_en_segundos = tiempo_natacion_hora_a_entero_a_segundo + tiempo_natacion_segundos_a_entero

print('tiempo natacion total, en segundo', tiempo_natacion_total_en_segundos)

## -----------------------------------------------------------

#HORA PEDESTRE A SEGUNDOS

tiempo_pedestre_hora_a_entero = tiempo_pedestre[0] + tiempo_pedestre[1]
tiempo_pedestre_hora_a_entero = int(tiempo_pedestre_hora_a_entero)
tiempo_pedestre_hora_a_entero_a_segundo = tiempo_pedestre_hora_a_entero * 60

print('tiempo pedestre hora a entero', tiempo_pedestre_hora_a_entero)

#SEGUNDOS PEDESTRE A ENTEROS

tiempo_pedestre_segundos_a_entero = tiempo_pedestre[-2] + tiempo_pedestre[-1]
tiempo_pedestre_segundos_a_entero = int(tiempo_pedestre_segundos_a_entero)

print('tiempo pedestre, de segundos a entero: ', tiempo_pedestre_segundos_a_entero)

#TIEMPO TOTAL PEDESTRE EN SEGUNDOS

tiempo_pedestre_total_en_segundos = tiempo_pedestre_hora_a_entero_a_segundo + tiempo_pedestre_segundos_a_entero

print('tiempo total en segundos, pedestre', tiempo_pedestre_total_en_segundos)

## -------------------------------------------------------------

#HORA CILISMO A SEGUNDOS

tiempo_ciclismo_hora_a_entero = tiempo_ciclismo[0] + tiempo_ciclismo[1]
tiempo_ciclismo_hora_a_entero = int(tiempo_ciclismo_hora_a_entero)

print('tiempo ciclismo hora a entero', tiempo_ciclismo_hora_a_entero)

tiempo_ciclismo_hora_a_entero_a_segundos = tiempo_ciclismo_hora_a_entero * 60

print('tiempo ciclismo hora a segundos', tiempo_ciclismo_hora_a_entero_a_segundos)

#SEGUNDOS CICLISMO A ENTERO

tiempo_ciclismo_segundos_a_enteros = tiempo_ciclismo[-2] + tiempo_ciclismo[-1]
tiempo_ciclismo_segundos_a_enteros = int(tiempo_ciclismo_segundos_a_enteros)

print('tiempo ciclismo, segundos a enteros', tiempo_ciclismo_segundos_a_enteros)

#TIEMPO TOTAL CICLISMO, EN SEGUNDOS

tiempo_ciclismo_total_en_segundos = tiempo_ciclismo_hora_a_entero_a_segundos + tiempo_ciclismo_segundos_a_enteros

print('tiempo de ciclismo total, en segundos: ', tiempo_ciclismo_total_en_segundos)

#TIEMPO TOTAL, EN SEGUNDOS, DE LOS TRES EVENTOS

tiempo_total_en_segundos_de_todos_los_eventos = tiempo_ciclismo_total_en_segundos + tiempo_pedestre_total_en_segundos + tiempo_natacion_total_en_segundos

print('tiempo total, en segundos, de los 3 eventos: ', tiempo_total_en_segundos_de_todos_los_eventos)



tiempo_total_a_horas = tiempo_total_en_segundos_de_todos_los_eventos // 3600
tiempo_total_a_minutos = (tiempo_total_en_segundos_de_todos_los_eventos % 3600) // 60
tiempo_total_a_segundos = (tiempo_total_en_segundos_de_todos_los_eventos % 3600) % 60

print(f'El tiempo total en horas es: {tiempo_total_a_horas}, en minutos es: {tiempo_total_a_minutos} y en segundos es: {tiempo_total_a_segundos}')















