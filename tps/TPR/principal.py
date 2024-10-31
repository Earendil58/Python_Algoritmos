from clase_serie import Serie

def menu():
    print('Por favor elija alguna de las siguientes opciones:')
    print('1) Generar vector ordenado de menor a mayor, por número de votos')
    print('2) Otra cosa')
    print('3) Tercera opcion')
    print('4) Cuarta opcion')
    print('5) Quinta opcion')
    print('6) Sexta opcion')
    print('7) Septima opcion')
    print('8) Salir')

    opcion = int(input('Ingrese su opcion: '))
    while opcion < 1 or opcion > 8:
        print(f'Por favor eliga entre alguna de las opciones disponibles, van del 1 al 8. Usted eligió erroneamente {opcion}')
        opcion = int(input('Ingrese su opcion: '))

    return opcion

def cargar_serie(linea):
    # Dividimos la línea por punto y coma
    datos = linea.split(';')

    # Solo procesamos si tiene duración de episodios
    if datos[4].strip() != "":
        # Quitamos la palabra "min" y convertimos a entero
        duracion = datos[4].replace('min', '').strip()

        # Creamos y retornamos el objeto Serie
        return Serie(
            datos[0],  # poster_link
            datos[1],  # series_title
            datos[2],  # runtime_of_series
            datos[3],  # certificate
            duracion,  # runtime_of_episodes (sin "min")
            datos[5],  # genre
            datos[6],  # imdb_rating
            datos[7],  # overview
            datos[12]  # no_of_vote (está después de los actores)
        )
    return None

def ordenar_vector(vector):
    n = len(vector)
    for i in range(n-1):
        for j in range(n-1-i):
            if vector[j].no_of_vote > vector[j+1].no_of_vote:
                # Intercambio
                vector[j], vector[j+1] = vector[j+1], vector[j]

def opcion_1():
    vector_series = []

    archivo = open('series_aed.csv', 'r', encoding='utf-8')

    # Saltamos la primera línea (cabecera)
    archivo.readline()

    # Leemos línea por línea
    linea = archivo.readline()
    while linea:
        # Intentamos crear una serie con la línea actual
        serie = cargar_serie(linea)

        # Si se pudo crear (tiene duración de episodios)
        if serie is not None:
            vector_series.append(serie)

        linea = archivo.readline()

    # Cerramos el archivo
    archivo.close()

    # Ordenamos el vector por número de votos
    ordenar_vector(vector_series)

    # Mostramos las series cargadas
    print(f"\nSe cargaron {len(vector_series)} series:")
    for serie in vector_series:
        print(str(serie))  # Cambiamos serie.to_string() por str(serie)

    return vector_series


def opcion_2(vector, m1, m2):
    series_minutos_entre_intervalo = []

    for serie in vector:
        if m1 <= serie.runtime_of_episodes <= m2:
            series_minutos_entre_intervalo.append(serie)

    for serie in series_minutos_entre_intervalo:
        print(serie)

def main():
    opcion_elegida = -1
    vector_series = []

    while opcion_elegida != 8:
        opcion_elegida = menu()

        if opcion_elegida == 1:
            vector_series = opcion_1()
            print("\nVector de series generado y ordenado por número de votos!")
            print()
            print()

        elif opcion_elegida == 2:
            if vector_series:
                m1 = int(input('Ingrese la cant de minutos de la cota inferior de búsqueda: '))
                m2 = int(input('Ingrese la cant de minutos de la cota superior de búsqueda: '))
                opcion_2(vector_series, m1, m2)

            else:
                print('Por favor primero ingrese la opción 1')



if __name__ == "__main__":
    main()
