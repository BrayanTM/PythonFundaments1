
#TODO Métodos y Funciones en los Diccionarios.

#? El método 'keys()'

"""

Este método devuelve una vista de todas las claves en el diccionario. Esto puede ser útil si deseas 
iterar sobre las claves o verificar si una clave específica existe.

Ejemplo:

"""

dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
print(dictionary.keys())  # Imprime dict_keys(['gato', 'perro', 'caballo'])
print("")

"""  

¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?

No y si.

Los diccionarios pueden ser iterados, pero no de la misma manera que las listas o tuplas. Cuando 
iteras sobre un diccionario, en realidad estás iterando sobre sus claves.

El método 'keys()' retorna o regresa una lista de todas las claves dentro del diccionario. Al tener 
una lista de claves se puede acceder a todo el diccionario de una manera fácil y útil.

A continuación se muestra un ejemplo:

"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
print("")

"""  

Otra manera de hacerlo es utilizar el método items(). Este método retorna una lista de tuplas (este 
es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) donde cada tupla es 
un par de cada clave con su valor.

"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)
print("")


#? Modificar, agregar y eliminar valores

"""  

Puedes modificar, agregar o eliminar valores en un diccionario de manera similar a como lo harías
con listas.

"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# Modificar un valor
dictionary["gato"] = "chat modificado"

# Agregar un nuevo par clave-valor
dictionary["pájaro"] = "oiseau"

# Eliminar un par clave-valor
del dictionary["perro"]

#? La función 'sorted()'

"""

La función 'sorted()' se puede utilizar para obtener una lista de las claves de un diccionario en 
orden. Esto es útil si deseas presentar las claves de una manera ordenada.

Ejemplo:

"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
print("")

"""  

También existe un método denominado values(), funciona de manera muy similar al de keys(), pero 
regresa una lista de valores.

"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for french in dictionary.values():
    print(french)
print("")


#? Agregando Nuevas Claves

"""  

Puedes agregar nuevas claves a un diccionario simplemente asignando un valor a una nueva clave.

Ejemplo:

"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary["pájaro"] = "oiseau"

print(dictionary)
print("")

# También es posible insertar un elemento al diccionario utilizando el método 'update()':

dictionary.update({"pez": "poisson"})
print(dictionary)
print("")

#? Eliminar Claves

"""  

Puedes eliminar una clave de un diccionario utilizando la instrucción 'del'.

Ejemplo:

"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary["perro"]

print(dictionary)
print("")

# También puedes utilizar el método 'pop()' para eliminar una clave y obtener su valor.

valor = dictionary.pop("caballo", "clave no encontrada")
print("Valor eliminado:", valor)
print(dictionary)
print("")

# Para eliminar el último elemento agregado
dictionary.popitem()
print(dictionary)

# También puedes utilizar el método 'clear()' para eliminar todos los elementos del diccionario.
dictionary.clear()
print(dictionary)