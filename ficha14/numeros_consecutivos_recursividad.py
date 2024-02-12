def consecutivos(n):
    if n > 0:
        consecutivos(n - 1)
        print(f'El número es: {n}')



consecutivos_diez = consecutivos(10)


