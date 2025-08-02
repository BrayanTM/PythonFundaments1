
#TODO Pseudocódigo e Introducción a Bucles

"""
El pseudocódigo es una herramienta útil para planificar y diseñar 
algoritmos antes de implementarlos en un lenguaje de programación 
específico. Permite expresar ideas de manera clara y concisa, sin 
preocuparse por la sintaxis exacta del código.

Un bucle es una estructura de control que permite repetir un bloque 
de código varias veces, ya sea un número específico de veces o 
hasta que se cumpla una condición determinada. Los bucles son 
fundamentales en la programación, ya que permiten automatizar tareas 
repetitivas y procesar colecciones de datos de manera eficiente.

"""

#? Ejemplo de pseudocódigo para un bucle

"""

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir a la línea 02

¿Qué está pasando en él?


En primer lugar, podemos simplificar el programa si, al principio del código, 
le asignamos a la variable largest_number un valor que será más pequeño que 
cualquiera de los números ingresados. Usaremos -999999999 para ese propósito.

En segundo lugar, asumimos que nuestro algoritmo no sabrá por adelantado 
cuántos números se entregarán al programa. Esperamos que el usuario ingrese 
todos los números que desee - el algoritmo funcionará bien con cien y con mil 
números. ¿Cómo hacemos eso?

Hacemos un trato con el usuario: cuando se ingresa el valor-1, será una señal 
de que no hay más datos y que el programa debe finalizar su trabajo.


De lo contrario, si el valor ingresado no es igual a -1, el programa leerá 
otro número, y así sucesivamente.

El truco se basa en la suposición de que cualquier parte del código se puede 
realizar más de una vez - precisamente, tantas veces como sea necesario.

La ejecución de una determinada parte del código más de una vez se denomina 
bucle. El significado de este término es probablemente obvio para ti.

Las líneas 02 al 08 forman un bucle. Los pasaremos tantas veces como sea 
necesario para revisar todos los valores ingresados.

¿Puedes usar una estructura similar en un programa escrito en Python? 
Si, si puedes.

"""

