import random

record_campeon = int(input('Ingrese el record del campeón: '))
retador_uno = ''
retador_dos = ''
nuevo_campeon = ''

#RONDA 1
primer_dado_ronda_uno = random.randint(1,6)
segundo_dado_ronda_uno = random.randint(1,6)

suma_dados_primera_ronda = primer_dado_ronda_uno + segundo_dado_ronda_uno

if (suma_dados_primera_ronda % 2) == 0:
    retador_dos = suma_dados_primera_ronda
    retador_uno = 0

else:
    retador_uno = suma_dados_primera_ronda
    retador_dos = 0

print(f'El retador uno, en la 1era RONDA sacó: {retador_uno} vs retador 2: {retador_dos}')


#RONDA 2
primer_dado_ronda_dos = random.randint(1,6)
segundo_dado_ronda_dos = random.randint(1,6)
mayor_puntaje_dado_ronda_dos = max(primer_dado_ronda_dos, segundo_dado_ronda_dos)
menor_puntaje_dado_ronda_dos = min(primer_dado_ronda_dos, segundo_dado_ronda_dos)

suma_dados_segunda_ronda = primer_dado_ronda_dos + segundo_dado_ronda_dos



if (suma_dados_segunda_ronda % 2) == 0:
    retador_dos += mayor_puntaje_dado_ronda_dos
    retador_uno -= menor_puntaje_dado_ronda_dos

else:
    retador_uno += mayor_puntaje_dado_ronda_dos
    retador_dos -= menor_puntaje_dado_ronda_dos

print(f'El retador uno, en la 2da RONDA sacó: {retador_uno} vs retador 2: {retador_dos}')

#GANADOR

if retador_uno > record_campeon and retador_uno > retador_dos:
    nuevo_campeon = [retador_uno, 'El retador uno']

elif retador_dos > record_campeon and retador_dos > retador_uno:
    nuevo_campeon = [retador_dos, 'El retador dos']

else:
    nuevo_campeon = [record_campeon, 'El campeón sigue siendo el viejo campeón']


print(f'Los dados que salieron en la PRIMER RONDA fueron, dado uno: {primer_dado_ronda_uno} y dado dos: {segundo_dado_ronda_uno}')
print(f'Los dados que salieron en la SEGUNDA RONDA fueron, dado uno: {primer_dado_ronda_dos} y dado dos: {segundo_dado_ronda_dos}')
print(f'El campeón es {nuevo_campeon}')
