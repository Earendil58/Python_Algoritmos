def alturas(cant_personas):
    alturas = []
    for persona in range(cant_personas):
        altura_persona = float(input(f'Ingrese la altura para la persona {persona + 1}: '))
        alturas.append(altura_persona)

    return alturas

def altura_media(alturas):
    acumulador_alturas = 0
    for i in alturas:
        acumulador_alturas += i

    estatura_media = round(acumulador_alturas / len(alturas), 2)
    return estatura_media


def contador_deltas_media(alturas, estatura_media):
    alturas_menores_media = alturas_mayores_media = alturas_iguales_media = 0
    for i in alturas:
        if i > estatura_media:
            alturas_mayores_media += 1
        elif i == estatura_media:
            alturas_iguales_media += 1
        else:
            alturas_menores_media += 1

    return alturas_mayores_media, alturas_iguales_media, alturas_menores_media




def principal():
    cant_personas = int(input('Ingrese la cant de personas a evaluar: '))
    alturas_personas = alturas(cant_personas)
    print(f'Alturas registradas: {alturas_personas}')
    altura_media_registrada = altura_media(alturas_personas)
    print(f'La altura media registrada es de: {altura_media_registrada} mts')
    cant_alturas_mayores_media, cant_alturas_iguales_media, cant_alturas_menores_media = contador_deltas_media(alturas_personas,altura_media_registrada)
    print(f'La cant de alturas mayores que la media son: {cant_alturas_mayores_media}')
    print(f'La cant de alturas iguales que la media son: {cant_alturas_iguales_media}')
    print(f'La cant de alturas menores que la media son: {cant_alturas_menores_media}')


if __name__ == '__main__':
    principal()
