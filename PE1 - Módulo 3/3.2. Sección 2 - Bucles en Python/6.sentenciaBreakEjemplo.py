
#TODO Sentencia Break - Ejemplo

"""

Regresemos a nuestro programa que reconoce el más grande entre 
los números ingresados. Lo convertiremos dos veces, usando las 
instrucciones de break y continue.

Analiza el código y determina como las usarías.

La variante empleando break es la siguiente:

"""

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

