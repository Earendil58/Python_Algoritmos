
def vector_conteo_generacion(longitud):
    vector_conteo = [0] * longitud
    return vector_conteo



def principal():
    longitud_vector_conteo = int(input('Ingrese la longitud del vector de conteo: '))
    vector_conteo = vector_conteo_generacion(longitud_vector_conteo)

    #CARGO NUMEROS EN VECTOR DE CONTEO:
    numero = int(input('Ingrese valores entre 0 y 99 [con -1 corta]: '))
    while numero != -1:
        if 0 <= numero < longitud_vector_conteo:
            vector_conteo[numero] += 1
        else:
            print(f'Te pasaste perro, la longitud era desde 0 hasta {longitud_vector_conteo}')

        numero = int(input('Ingrese valores entre 0 y 99 [con -1 corta]: '))

    for i in range(len(vector_conteo)):
        if vector_conteo[i] != 0:
            print(f'Numero: {i} - Frecuencia de aparición: {vector_conteo[i]}')


if __name__ == '__main__':
    principal()
