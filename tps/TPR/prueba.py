from clase_serie import Serie

def cargar_serie(linea):
    datos = linea.split(";")

    if datos[4].strip() != "":
        duracion = datos[4].strip().replace("min", "")

        return Serie(
            datos[0],
            datos[1],
            datos[2],
            datos[3],
            duracion,
            datos[5],
            datos[6],
            datos[7],
            datos[12]
        )

    return None


def ordenar_vector(vector):
    longitud_vector = len(vector)

    for i in range(longitud_vector - 1):
        for j in range(longitud_vector - 1 - i):
            if vector[j].no_of_vote > vector[j + 1].no_of_vote:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]


def generar_vector_series():
    vector_series = []

    archivo = open('series_aed.csv', 'r', encoding='utf-8')

    # salto la primera línea
    archivo.readline()

    linea = archivo.readline()
    while linea:
        serie = cargar_serie(linea)

        if serie is not None:
            vector_series.append(serie)

        linea = archivo.readline()

    archivo.close()

    ordenar_vector(vector_series)

    for serie in vector_series:
        print(serie)


if __name__ == '__main__':
    generar_vector_series()
