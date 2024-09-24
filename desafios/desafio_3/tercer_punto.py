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

# Paso 2: Encontrar el valor modal y su frecuencia de aparición
max_frecuencia = max(cont)  # Encontramos la frecuencia máxima
moda = 0  # Inicializamos la variable moda como 0 (en caso de que no haya una única moda)
frecuencia_modal = 0  # Inicializamos la frecuencia modal como 0 (en caso de que no exista moda)
count_max = cont.count(max_frecuencia)  # Contamos cuántos números tienen la frecuencia máxima

# Si hay solo un número con la frecuencia máxima, encontramos la moda
if count_max == 1:
    idx_moda = cont.index(max_frecuencia)  # Buscamos el índice del número con la frecuencia máxima
    moda = num[idx_moda]  # El número modal es el que está en la misma posición en num
    frecuencia_modal = max_frecuencia  # La frecuencia del valor modal es la máxima frecuencia

# Resultado final: valor modal y su frecuencia de aparición
print(f'El valor modal es: {moda}')
print(f'La frecuencia de aparición del valor modal es: {frecuencia_modal}')
