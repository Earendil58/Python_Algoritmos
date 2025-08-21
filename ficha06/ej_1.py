# Complejo de cines
# Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce: cantidad de espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).
# El programa deberá:
# a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con descuento y $75 en los días sin descuento.
# b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones.

from typing import Literal

Tipo_Descuento = Literal['descuento', 'sin descuento']
VALIDOS = {'descuento', 'sin descuento'}

def calcular_recaudacion(cant_espectadores: int, descuento: Tipo_Descuento) -> int:
    VALOR_ENTRADA_SIN_DESCUENTO = 75
    VALOR_ENTRADA_CON_DESCUENTO = 50

    if descuento == 'descuento':
        calculo_recaudacion = cant_espectadores * VALOR_ENTRADA_CON_DESCUENTO
    else:
        calculo_recaudacion = cant_espectadores * VALOR_ENTRADA_SIN_DESCUENTO

    return calculo_recaudacion


def main():
    recaudacion_total = 0
    total_funciones = 0
    funciones_con_descuento = 0

    print("Carga de funciones (0 espectadores para terminar):")
    while True:
        espectadores = int(input("Cantidad de espectadores: "))
        if espectadores == 0:
            break

        descuento = input("La función tiene descuento (descuento/sin descuento)? ").strip().lower()

        recaudacion_total += calcular_recaudacion(espectadores, descuento)
        total_funciones += 1
        if descuento == "descuento":
            funciones_con_descuento += 1

    # Resultados
    print(f"\nRecaudación total: ${recaudacion_total}")
    if total_funciones > 0:
        porcentaje = funciones_con_descuento * 100 / total_funciones
        print(f"Funciones con descuento: {funciones_con_descuento} de {total_funciones} "
              f"({porcentaje:.2f}%)")

if __name__ == "__main__":
    main()