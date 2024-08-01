def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio  # Elemento encontrado, devolver el índice
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # Elemento no encontrado

# Ejemplo de uso
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
objetivo = 7
indice = busqueda_binaria(arr, objetivo)
print("Índice del objetivo:", indice)
