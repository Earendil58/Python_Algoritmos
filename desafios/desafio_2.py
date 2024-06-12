def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)  # Añadir el 1 al final de la secuencia

    # Calcular estadísticas
    length = len(sequence)
    max_value = max(sequence)
    average = sum(sequence) / length

    return sequence, length, average, max_value

# Función para formatear el promedio
def format_average(average):
    return round(average, 1)

# Ejecución y pruebas con los valores dados
test_values = [13251, 234519, 9386]

for n in test_values:
    sequence, length, average, max_value = collatz_sequence(n)
    print(f"\nn = {n}")
    print(f"Órbita de n = {n} (valores calculados incluyendo al {n} y al 1): {sequence}")
    print(f"Longitud de la órbita (cantidad de valores calculados hasta llegar al 1): {length}")
    print(f"Promedio de todos los valores de la órbita: {format_average(average)}")
    print(f"Mayor de los números en esa órbita: {max_value}")
