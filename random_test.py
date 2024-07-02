def ordenar(n1, n2, desc = True):
    menor, mayor = n1, n2

    if desc:
        if n1 < n2:
            menor, mayor = n1, n2
    else:
        menor, mayor = n2, n1

    return menor, mayor



ordenamiento = ordenar(1,2, False)

print(ordenamiento)


