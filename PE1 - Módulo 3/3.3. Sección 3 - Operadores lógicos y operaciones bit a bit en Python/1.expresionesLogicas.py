
#TODO Expresiones lógicas

var = 1

# Ejemplo 1:
print(var > 0)
print(not (var <= 0))


# Ejemplo 2:
print(var != 0)
print(not (var == 0))

"""  

Las leyes de Morgan dicen que:

- La negación de una conjunción es la disyunción de las negaciones:

    not (A and B)  <=>  (not A) or (not B)

- La negación de una disyunción es la conjunción de las negaciones:

    not (A or B)  <=>  (not A) and (not B)

Ninguno de estos operadores de dos argumentos se puede usar en la forma abreviada
conocida como op= (+=, -=, ...).

"""

#? Valores lógicos vs bits individuales

"""  

Los operadores lógicos toman sus argumentos como todo, independientemente de
cuantos bits contengan. Los operadores solo conocen el valor: cero (cuando todos
los bits se restablecen) significa False; no cero (cuando se establece al menos
un bit) significa True.

El resultado de sus operaciones es uno de estos valores: False o True. Esto 
significa que este fragmento de código asignará el valor True a la variable j si
i no es cero; de lo contrario, asignará False:

i = 1
j = not not i

"""

i = 1
j = not not i

print(j)  # True