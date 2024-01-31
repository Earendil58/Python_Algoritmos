import random

dado_uno = random.randint(1,6)
dado_dos = random.randint(1,6)

suma_dados = dado_uno + dado_dos

if dado_uno == dado_dos or (suma_dados % 2) != 0:
    print(f'Usted gana, los dados salieron: {dado_uno} y {dado_dos}')

else:
    print(f'Usted pierde, los dados salieron: {dado_uno} y {dado_dos}')
