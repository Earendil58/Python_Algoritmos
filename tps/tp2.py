import random

print('♠♦♥♣' * 15 + ' BlackJack ' + '♠♦♥♣' * 15)
print('Bienvenido al juego de BlackJack')
# ENTRADAS

nombre = input('Indique su nombre: ')
monto = float('Ingrese el monto a apostar: ')

dinero_apuesta = 0

#MOSTRAMOS LAS OPCIONES DEL JUEGO
print('Elija una opción, {}:'.format(nombre))
print('1) Haga una apuesta.')
print('2) Juegue una mano.')
print('3) Salir del juego. ')

#ELEJIMOS LAS OPCIONES:
opcion = input('Elija alguna de las opciones anteriores: ')

#INICIALIZAMOS LAS CARTAS
numero = 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'
palo = '♠ Pica ♠', ' ♦ Diamante ♦', '♥ Corazon ♥', '♣ Trebol ♣'
se_planta_crupier, hay_figuras, empate = True, False, False
bjack = 21
ptaje_1 = 0
ptaje_2 = 0
men = 0
may = 0
carta1_jg = random.choice(numero), random.choice(palo)
carta2_jg = random.choice(numero), random.choice(palo)
carta3_jg = random.choice(numero), random.choice(palo)

carta1_cr = random.choice(numero), random.choice(palo)
carta2_cr = random.choice(numero), random.choice(palo)
carta3_cr = random.choice(numero), random.choice(palo)


#-----------------------------------------------------------------
if opcion==1:
    if monto<=0:
        while monto<=0:
            monto += input('Ingrese el monto a adicionar a su pozo: ')

    else:
        monto += input('Ingrese el monto a adicionar a su pozo: ')

elif opcion==2:
    if monto>0:
        print('Cuanto quieras apostar? (recuerda que puedes jugar multiplos de 5!)')
        dinero_apuesta=float(input('Cuanto quieras apostar?: '))
        if dinero_apuesta<=monto:
            monto -= dinero_apuesta
        else:
            while dinero_apuesta>monto:
                print('No puedes apostar más de lo que tienes, por favor ingresa un monto válido')
            dinero_apuesta=float(input('Cuanto quieras apostar?: '))
            monto -= dinero_apuesta

    else:
        print('Usted no tiene más dinero para apostar o ingresar en su pozo.')

