
#TODO Recursividad

"""  

La recursividad es una técnica en programación donde una función se llama a sí misma para resolver 
un problema. Es especialmente útil para problemas que pueden ser divididos en subproblemas más 
pequeños del mismo tipo.

La serie de Fibonacci es un ejemplo clásico de un problema que se puede resolver de manera recursiva.

"""

def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Salida: 8 (la secuencia es 1, 1, 2, 3, 5, 8, ...)
print("")

# El factorial también se puede calcular de manera recursiva.
def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Salida: 120 (5 * 4 * 3 * 2 * 1)
print("")

