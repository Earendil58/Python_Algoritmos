import soporte  # Importamos el módulo proporcionado por la cátedra

# Paso 1: Generamos el arreglo de entrada con 300000 números
v = soporte.vector_unknown_range(300000)

# Inicializamos los arreglos vacíos num y cont
num = []  # Para almacenar los números distintos
cont = []  # Para contar las veces que cada número aparece

# Procesamos cada número en el arreglo v
for x in v:
    # Intentamos buscar el número x en el arreglo num
    if x in num:
        # Si x ya está en num, incrementamos su contador en cont
        idx = num.index(x)
        cont[idx] += 1
    else:
        # Si x no está en num, lo agregamos y establecemos su contador en 1
        num.append(x)
        cont.append(1)

# Mostramos la cantidad de números diferentes
print(f'Cantidad de números diferentes: {len(num)}')
