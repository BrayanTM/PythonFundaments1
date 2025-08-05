
#TODO Bucles con while

"""

En general, en python, un bucle se puede representar de la siguiente manera:

while
    instruction

Si se observan algunas similitudes con la instrucción if, está bien. De hecho,
la diferencia sintáctica es solo una: usa la palabra "while" en lugar de "if".

La diferencia semántica es más importante: cuando se cumple la conidción, if
realiza sus sentencias sólo una vez; while repite la ejecución siempre que la 
condición se evalue como True.

while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n

Ahora, es importante recordar que:

- si deseas ejecutar más de una sentencia dentro de un while, debes (como con if) 
  poner sangría a todas las instrucciones de la misma manera.
- una instrucción o conjunto de instrucciones ejecutadas dentro del while se llama 
  el cuerpo del bucle.
- si la condición es False (igual a cero) tan pronto como se compruebe por primera 
  vez, el cuerpo no se ejecuta ni una sola vez (ten en cuenta la analogía de no 
  tener que hacer nada si no hay nada que hacer).
- el cuerpo debe poder cambiar el valor de la condición, porque si la condición es 
  True al principio, el cuerpo podría funcionar continuamente hasta el infinito. 
  Observa que hacer una cosa generalmente disminuye la cantidad de cosas por hacer.
    
"""

#TODO Bucle infinito

"""

Un bucle infinito, también denominado bucle sin fin, es una secuencia de 
instrucciones en un programa que se repite indefinidamente (bucle sin fin).

Este es un ejemplo de un bucle que no puede finalizar su ejecución:

while True:
    print("Estoy atrapado dentro de un bucle.")

"""

# Almacena el actual número más grande aquí.
largest_number = -999999999
 
# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Imprime el número más grande.
print("El número más grande es:", largest_number)