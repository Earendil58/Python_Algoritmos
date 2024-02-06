def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial_cinco = factorial(5)

print(f'El factorial de 5 es: {factorial_cinco}')
