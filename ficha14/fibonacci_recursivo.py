
def fibonacci(limite):
    ant_1 = ant_2 = 1

    for i in range(2, limite + 1):
        aux = ant_1 + ant_2
        ant_2 = ant_1
        ant_1 = aux
        print(ant_2)




    print(f'El acumulado de los número Fibonacci fue de: {ant_1}')



fibonacci(100)
