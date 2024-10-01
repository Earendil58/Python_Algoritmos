def quicksort(array):
    # Caso base: Si la lista tiene un solo elemento o está vacía, ya está ordenada
    if len(array) <= 1:
        return array

    # Elegimos el pivote, aquí elegimos el primer elemento (podrías elegir cualquiera)
    pivot = array[0]

    # Particionar: Dividimos en tres listas - menores, iguales, mayores
    menores = [x for x in array[1:] if x < pivot]  # Todos los elementos menores al pivote
    iguales = [x for x in array if x == pivot]     # Todos los elementos iguales al pivote
    mayores = [x for x in array[1:] if x > pivot]  # Todos los elementos mayores al pivote

    # Llamada recursiva a quicksort sobre las sublistas y concatenar el resultado
    return quicksort(menores) + iguales + quicksort(mayores)



arreglo = [41,74,78,1,0,101,-14,-11,3,5,9]

arreglo_ordenado = quicksort(arreglo)

print(arreglo_ordenado)
