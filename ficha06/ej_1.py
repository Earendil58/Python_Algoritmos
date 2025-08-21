# Complejo de cines
# Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce: cantidad de espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).
# El programa deberá:
# a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con descuento y $75 en los días sin descuento.
# b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones.

from typing import Literal

tipo_validez = Literal['descuento', 'sin descuento']
VALIDOS = {'descuento', 'sin descuento'}

def calculo_cine(cant_espectadores, descuento):
    VALOR_ENTRADA_SIN_DESCUENTO = 75
    VALOR_ENTRADA_CON_DESCUENTO = 50
    calculo_recaudacion = 0


    if descuento == 'descuento':
        calculo_recaudacion = cant_espectadores * VALOR_ENTRADA_CON_DESCUENTO
    else:
        calculo_recaudacion = cant_espectadores * VALOR_ENTRADA_SIN_DESCUENTO
    return calculo_recaudacion


def main():
    cant_de_funciones = int(input('Ingrese la cantidad de funciones: '))
    recaudación_total_de_funciones = 0

    if cant_de_funciones == 0:
        print('No hubo funciones')

    else:
        for funcion in range(cant_de_funciones):
            cantidad_de_espectadores = int(input('Ingrese cant de espectadores: '))
            while True:
                descuento : tipo_validez = (input('La función tiene descuento (descuento/sin descuento)? :').strip().lower())
                if descuento in VALIDOS:
                    break
                print("Tipo inválido, intenta otra vez (descuento/sin descuento)")

            recaudación_total_de_funciones += calculo_cine(cantidad_de_espectadores, descuento)

        print(f'La recaudacion total de las funciones realizadas fue de ${recaudación_total_de_funciones}')





if __name__ == "__main__":
    main()

