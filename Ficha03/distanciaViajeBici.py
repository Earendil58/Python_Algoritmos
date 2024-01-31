dist_km_pts_extremos_arg = 3641.3

metros_recorridos_accidente = float(input('Ingrese cuantos metros recorrio hasta que se accidentó: '))

#PASO DE MTS A KMS
kms_recorridos_accidente = metros_recorridos_accidente/1000

#PORCENTAJE RECORRIDO
porcentaje = (kms_recorridos_accidente * 100) / dist_km_pts_extremos_arg

print('Usted recorrió: {}mts, en km son: {:.2f}kms y el porcentaje que representa, en kms es {:.2f}%'.format(metros_recorridos_accidente, kms_recorridos_accidente,porcentaje))



