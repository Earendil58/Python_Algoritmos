import soporte  # Importamos el módulo proporcionado por la cátedra

# Paso 1: Generamos el arreglo de entrada con 300000 números, en un rango conocido [0..299999]
v = soporte.vector_known_range(300000)

# Paso 2: Creamos un arreglo c de 300000 casillas, inicializadas en cero
c = [0] * 300000  # Arreglo de conteo directo

# Paso 3: Contamos las ocurrencias de cada número en el arreglo v
for x in v:
    c[x] += 1  # Incrementamos la casilla correspondiente en el arreglo c

# Paso 4: Contamos cuántos números diferentes (casilleros diferentes de cero) hay en el arreglo c
numeros_diferentes = sum(1 for count in c if count > 0)

# Resultado final: cantidad de números diferentes
print(f'Cantidad de números diferentes: {numeros_diferentes}')
