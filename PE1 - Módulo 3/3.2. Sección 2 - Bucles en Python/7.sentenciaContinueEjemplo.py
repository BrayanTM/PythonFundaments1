
#TODO Sentencia Continue - Ejemplo

"""

Regresemos a nuestro programa que reconoce el más grande entre 
los números ingresados. Lo convertiremos dos veces, usando las 
instrucciones de break y continue.

Analiza el código y determina como las usarías.

La variante empleando continue es la siguiente:

"""

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")



