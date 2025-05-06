# Calcular factorial usando un bucle for
def factorial_for(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Calcular factorial usando un bucle while
def factorial_while(n):
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += 1
    return resultado

# Pedir al usuario un número
numero = int(input("Ingresa un número para calcular su factorial: "))

# Mostrar resultados
print(f"Factorial de {numero} usando for: {factorial_for(numero)}")
print(f"Factorial de {numero} usando while: {factorial_while(numero)}")
