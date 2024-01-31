cuadro_uno = int(input('Ingresa el año del primer cuadro: '))
cuadro_dos = int(input('Ingresa el año del segundo cuadro: '))
cuadro_tres = int(input('Ingresa el año del tercer cuadro: '))
año_busqueda = int(input('Ingrese el año de busqueda, para ver si alguno de los cuadros se corresponde con él: '))


#SI ALGUNA DE LAS OBRAS ES ANTERIOR AL SIGLO XX
siglo_veinte_inicio = 1901

if cuadro_uno < siglo_veinte_inicio and cuadro_dos < siglo_veinte_inicio and cuadro_tres < siglo_veinte_inicio:
    print(f'Todos los cuadros son anteriores al siglo XX')
elif not(cuadro_uno < siglo_veinte_inicio or cuadro_dos < siglo_veinte_inicio or cuadro_tres < siglo_veinte_inicio):
    print('Ningun cuadro es anterior al siglo XX')
else:
    print('Al menos uno de los cuadros no es anterior al siglo XX')

# DIFIRENCIA DE AÑOS ENTRE EL CUADRO MAS VIEJO Y EL MAS NUEVO

menor = ''
mayor = ''

if cuadro_uno < cuadro_dos and cuadro_uno < cuadro_tres:
    menor = cuadro_uno
    if cuadro_tres > cuadro_dos:
        mayor = cuadro_tres
    else:
        mayor = cuadro_dos
if cuadro_dos < cuadro_uno and cuadro_dos < cuadro_tres:
    menor = cuadro_dos
    if cuadro_uno > cuadro_tres:
        mayor = cuadro_uno
    else:
        mayor = cuadro_tres
if cuadro_tres < cuadro_uno and cuadro_tres < cuadro_dos:
    menor = cuadro_tres
    if cuadro_uno > cuadro_dos:
        mayor = cuadro_uno
    else:
        mayor = cuadro_dos

diferencia_entre_cuadros = mayor - menor

# BUSQUEDA DE CUADRO, POR AÑO



if año_busqueda in (cuadro_uno, cuadro_dos, cuadro_tres):
    print(f'Si hay cuadros correspondientes al año: {año_busqueda}')

print(f'El cuadro más reciente es: {mayor} y el más antiguo es: {menor}')
print(f'La diferencia, en años, entre ellos es de: {diferencia_entre_cuadros}')







