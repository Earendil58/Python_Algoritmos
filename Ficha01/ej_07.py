MONTO_BASE = 1500

cant_km_recorridos = int(input('Ingrese la cant de km recorridos: '))

monto_total = MONTO_BASE + (0.3 * cant_km_recorridos)

print(f'El monto total es de ${monto_total}, por una cant de km recorridos de {cant_km_recorridos} km')


