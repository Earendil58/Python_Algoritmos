from clase_serie import Serie
import pickle
import os

def menu():
    print("Por favor elija alguna de las siguientes opciones:")
    print("1) Generar vector ordenado de menor a mayor, por número de votos")
    print("2) Filtrar series por duración y calcular promedio")
    print("3) Generar vector de géneros únicos")
    print("4) Contar series por cada género")
    print("5) Guardar géneros y conteo en archivo binario")
    print("6) Mostrar el archivo binario generado")  # Requiere haber ejecutado opciones 1, 3, 4 y 5.
    print("7) Buscar una serie por título y actualizar votos")
    print("8) Salir")

    # Recordatorio para el usuario
    print("\nNota: Para ejecutar la opción 6, primero debe ejecutar las opciones 1, 3, 4 y 5.\n")

    opcion = int(input("Ingrese su opción: "))
    while opcion < 1 or opcion > 8:
        print(f"Por favor elija entre alguna de las opciones disponibles (1-8). Usted eligió {opcion}, que es incorrecto.")
        opcion = int(input("Ingrese su opción: "))

    return opcion


def cargar_serie(linea):
    datos = linea.split(';')

    if datos[4].strip() != "":
        duracion = int(datos[4].replace('min', '').strip())

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
                vector[j], vector[j+1] = vector[j+1], vector[j]

def opcion_1():
    vector_series = []

    archivo = open('series_aed.csv', 'r', encoding='utf-8')

    archivo.readline()

    linea = archivo.readline()
    while linea:
        serie = cargar_serie(linea)

        if serie is not None:
            vector_series.append(serie)

        linea = archivo.readline()

    archivo.close()

    ordenar_vector(vector_series)

    print(f"\nSe cargaron {len(vector_series)} series:")
    for serie in vector_series:
        print(str(serie))

    return vector_series


def opcion_2(vector, m1, m2, desea_guardar):
    series_minutos_entre_intervalo = []
    sumatoria_minutos_series_entre_intervalo = 0
    cant_series_entre_intervalo = 0

    for serie in vector:
        if m1 <= serie.runtime_of_episodes <= m2:
            series_minutos_entre_intervalo.append(serie)
            sumatoria_minutos_series_entre_intervalo += serie.runtime_of_episodes
            cant_series_entre_intervalo += 1

    if cant_series_entre_intervalo > 0:
        promedio = round(sumatoria_minutos_series_entre_intervalo / cant_series_entre_intervalo, 2)
        print(f'La duración, en promedio, de las series entre el intervalo ingresado es de: {promedio} minutos')
        print()

        for serie in series_minutos_entre_intervalo:
            print(serie)

    if desea_guardar == 'si':
        archivo_nombre = input('Ingrese un nombre para el archivo .csv: ') + '.csv'
        with open(archivo_nombre, "w", encoding='utf-8') as archivo_csv:
            archivo_csv.write("title;runtime_series;certificate;runtime_episodes;genre;imdb_rating;overview;no_of_votes\n")
            for serie in series_minutos_entre_intervalo:
                archivo_csv.write(f"{serie.series_title};{serie.runtime_of_series};{serie.certificate};{serie.runtime_of_episodes};"
                                  f"{serie.genre};{serie.imdb_rating};{serie.overview};{serie.no_of_vote}\n")
            print(f"Archivo {archivo_nombre}' guardado con éxito.")

            
def opcion_3(vector_series):
    generos_unicos = []
    for serie in vector_series:
        genero = serie.genre.strip()
        if genero not in generos_unicos:
            generos_unicos.append(genero)

    print(f'Generos listos!')
    return generos_unicos


def opcion_4(vector_series, generos_unicos):
    conteo_por_genero = [0] * len(generos_unicos)


    for serie in vector_series:
        genero_serie = serie.genre.strip()

        indice_genero = -1
        for i in range(len(generos_unicos)):
            if generos_unicos[i] == genero_serie:
                indice_genero = i
                break

        if indice_genero != -1:
            conteo_por_genero[indice_genero] += 1

    print("Conteo de series por género:")
    for i in range(len(generos_unicos)):
        print(f"Género {i + 1} ({generos_unicos[i]}): {conteo_por_genero[i]} series")

    return conteo_por_genero


def opcion_5(generos_unicos, conteo_por_genero, nombre_archivo="generos.csv"):
    datos_generos = []

    for i in range(len(generos_unicos)):
        genero_info = {
            "numero": i + 1,                  # Número del género (inicia en 1)
            "nombre": generos_unicos[i],      # Nombre del género
            "cantidad": conteo_por_genero[i]  # Cantidad de series de este género
        }
        datos_generos.append(genero_info)

    with open(nombre_archivo, "wb") as archivo_binario:
        pickle.dump(datos_generos, archivo_binario)

    print(f"Archivo binario '{nombre_archivo}' guardado con éxito.")


def opcion_6(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "rb") as archivo_binario:
            datos_generos = pickle.load(archivo_binario)

        print("Contenido del archivo binario:")
        for genero_info in datos_generos:
            print(f"Número: {genero_info['numero']}, "
                  f"Género: {genero_info['nombre']}, "
                  f"Cantidad de series: {genero_info['cantidad']}")
    else:
        print(f"El archivo '{nombre_archivo}' no existe. Por favor, ejecute la opción 5 primero para generarlo.")


def opcion_7(vector_series):
    tit = input("Ingrese el título de la serie a buscar: ")
    encontrada = False

    for serie in vector_series:
        if serie.series_title.lower() == tit.lower():
            serie.no_of_vote += 1
            print(f"\nSe incrementó en 1 el número de votos para la serie '{serie.series_title}'")
            print(f"Nuevo número de votos: {serie.no_of_vote}")
            encontrada = True
            break

    if not encontrada:
        print(f"\nNo se encontró ninguna serie con el título '{tit}'")





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
                desea_guardar_series_filtradas = input('Desea guardar las series filtradas? (si/no): ')
                while desea_guardar_series_filtradas.lower() != 'si' and desea_guardar_series_filtradas.lower() != 'no':
                    print(f'Esto es lo que hay en desea_guardar: {desea_guardar_series_filtradas}')
                    print('Por favor brinde una respuesta de si o no')
                    desea_guardar_series_filtradas = input('Desea guardar las series filtradas? (si/no): ')
                opcion_2(vector_series, m1, m2, desea_guardar_series_filtradas)
                print()
                print()

            else:
                print('Por favor primero ingrese la opción 1')

        elif opcion_elegida == 3:
            if vector_series:
                generos_unicos = opcion_3(vector_series)
                print()
                print()

            else:
                print("Primero ejecute la opción 1 para cargar las series.")
                print()
                print()

        elif opcion_elegida == 4:
            if vector_series and generos_unicos:
                conteo_por_genero = opcion_4(vector_series, generos_unicos)
                print()
                print()
            else:
                print('Por favor primero ingrese la opción 1 y la 3')
                print()
                print()

        elif opcion_elegida == 5:
            if generos_unicos and conteo_por_genero:
                nombre_archivo_punto_5 = input('Ingrese un nombre para el archivo a generar: ') + '.csv'
                opcion_5(generos_unicos, conteo_por_genero, nombre_archivo_punto_5)
                print()
                print()
            else:
                print("Primero ejecute las opciones 3 y 4 para generar los géneros y el conteo de series.")
                print()
                print()

        elif opcion_elegida == 6:
            if vector_series and generos_unicos and conteo_por_genero and nombre_archivo_punto_5:
                opcion_6(nombre_archivo_punto_5)
                print()
                print()
            else:
                print('Por favor primero ingrese la opción 1. luego la 3, la 4 y por último la 5 antes de volver a seleccionar la opción 6')
                print()
                print()

        elif opcion_elegida == 7:
            if vector_series:
                opcion_7(vector_series)
                print()
                print()
            else:
                print('Primero genere el vector, ingresando primero la opción 1')
                print()
                print()

    print('Programa terminado. Hasta luego!')


if __name__ == "__main__":
    main()
