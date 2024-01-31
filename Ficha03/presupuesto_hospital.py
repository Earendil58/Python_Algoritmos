presupuesto_total_hospital = float(input('Ingrese el monto dispuesto para el hospital: '))

presupuesto_pediatria = presupuesto_total_hospital * 0.42
presupuesto_urgencia = presupuesto_total_hospital * 0.37
presupuesto_traumatologia = presupuesto_total_hospital * 0.21

print(f'El presupuesto para cada area del hospital es: ')
print(f'Urgencia: {presupuesto_urgencia}')
print(f'Pediatria: {presupuesto_pediatria}')
print(f'Traumatologia: {presupuesto_traumatologia}')
