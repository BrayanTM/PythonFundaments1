
#TODO Numeros Fibonacci

"""  

La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos anteriores. 
Comienza típicamente con 0 y 1. Así que la secuencia se ve así:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Vamos a definir una función que calcule el n-ésimo número de Fibonacci.

"""

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 11):  # probando
    print(n, "->", fib(n))

