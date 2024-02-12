def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Solicitar al usuario el término de Fibonacci deseado
n = int(input("Ingrese el término de Fibonacci deseado: "))

# Validar la entrada
if n < 0:
    print("Por favor, ingrese un número entero no negativo.")
else:
    result = fibonacci(n)
    print(f"El término {n} de la secuencia de Fibonacci es: {result}")
