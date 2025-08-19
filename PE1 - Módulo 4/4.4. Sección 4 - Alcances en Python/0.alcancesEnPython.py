
#TODO Los Alcances en Python

#? Funciones y Alcances

"""  

En Python, el alcance de una variable se refiere a la región del código donde esa variable es 
accesible. Existen diferentes tipos de alcances:

- Alcance de función: Las variables definidas dentro de una función son accesibles solo dentro 
  de esa función.
- Alcance de módulo: Las variables definidas en un módulo son accesibles en todo el módulo.
- Alcance global: Las variables definidas en el nivel más alto de un script son accesibles 
  en todo el script.

Una variable que existe fuera de una función tiene un alcance dentro del cuerpo de la función, 
excluyendo a aquellas que tienen el mismo nombre.

También significa que el alcance de una variable existente fuera de una función solo se puede 
implementar dentro de una función cuando su valor es leído. El asignar un valor hace que la 
función cree su propia variable.
  
"""

# Ejemplo de alcance de variable, fuera de una función
def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)

# Ejemplo de alcance de variable, dentro de una función
def my_function2():
    var = 2
    print("¿Conozco a la variable?", var)


var = 1
my_function2()
print(var)
print("")

#? Función y Alcances: La Palabra Clave "global"

"""  

La palabra clave "global" se utiliza para declarar que una variable dentro de una función 
es global, lo que significa que puede acceder y modificar la variable global con el mismo 
nombre.

El utilizar la palabra reservada dentro de una función con el nombre o nombres de las 
variables separados por comas, obliga a Python a abstenerse de crear una nueva variable 
dentro de la función - se empleará la que se puede acceder desde el exterior.

En otras palabras, este nombre se convierte en global (tiene un alcance global, y no importa 
si se esta leyendo o asignando un valor).

"""

def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)
print("")


#? Cómo Interactúa la Función con sus Argumentos?

"""  

Al cambiar el valor del parámetro este no se propaga fuera de la función (más específicamente, 
no cuando la variable es un valor escalar).

Esto también significa que una función recibe el valor del argumento, no el argumento en sí. 
Esto es cierto para los valores escalares.

El siguiente ejemplo arrojará luz sobre el asunto:

"""

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

"""  

Parece ser que se sigue aplicando la misma regla.

Finalmente, la diferencia se puede observar en el siguiente ejemplo:

"""

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Presta atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

"""  

No se modifica el valor del parámetro my_list_1 (ya se sabe que no afectará el argumento), en lugar 
de ello se modificará la lista identificada por el.

El resultado puede ser sorprendente. Ejecuta el código y verifícalo:

Output
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [3]
Print #4: [3]
Print #5: [3]

¿Lo puedes explicar?

Intentémoslo:

- si el argumento es una lista, el cambiar el valor del parámetro correspondiente no afecta la lista 
  (recuerda: las variables que contienen listas son almacenadas de manera diferente que las escalares)
- pero si se modifica la lista identificada por el parámetro (nota: ¡la lista, no el parámetro!), la 
  lista reflejará el cambio.

"""