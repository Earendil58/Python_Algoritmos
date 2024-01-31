costo_total_proyecto = float(input('Ingrese el costo total del proyecto: '))

costos_del_sistema = costo_total_proyecto * 0.17

costo = costo_total_proyecto - costos_del_sistema

print(f'Los costos del proyecto no deben exceder los ${costo}')
