def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag para optimizar el algoritmo
        swapped = False

        for j in range(0, n-i-1):
            # Comparar elementos adyacentes
            if arr[j] > arr[j+1]:
                # Intercambiar si están en el orden incorrecto
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # Si no hubo intercambios, la lista está ordenada
        if not swapped:
            break

    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)
