import soporte  # Importamos el módulo proporcionado por la cátedra

# Paso 1: Generamos el arreglo de entrada con 300000 números, en un rango conocido [0..299999]
v = soporte.vector_known_range(300000)

# Paso 2: Creamos un arreglo c de 300000 casillas, inicializadas en cero
c = [0] * 300000  # Arreglo de conteo directo

# Paso 3: Contamos las ocurrencias de cada número en el arreglo v
for x in v:
    c[x] += 1  # Incrementamos la casilla correspondiente en el arreglo c

# Paso 4: Determinamos el valor modal y su frecuencia
max_frecuencia = max(c)  # Obtenemos la frecuencia máxima
moda = 0  # Inicializamos el valor modal en 0
frecuencia_modal = 0  # Inicializamos la frecuencia de la moda en 0
count_max = c.count(max_frecuencia)  # Contamos cuántos números tienen la frecuencia máxima

# Si hay solo un número con la frecuencia máxima, determinamos el valor modal y su frecuencia
if count_max == 1:
    moda = c.index(max_frecuencia)  # Buscamos el índice del número con la frecuencia máxima
    frecuencia_modal = max_frecuencia  # La frecuencia del valor modal es la máxima frecuencia

# Resultado final: valor modal y su frecuencia
print(f'El valor modal es: {moda}')
print(f'La frecuencia de aparición del valor modal es: {frecuencia_modal}')
