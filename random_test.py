def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array



def main():
    array_a_ordenar = [7,5,12,101,1,3,14]
    array_ordenado = bubble_sort(array_a_ordenar)

    print(array_ordenado)



if __name__ == '__main__':
    main()
