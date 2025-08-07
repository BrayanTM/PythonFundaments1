
#TODO Agregar elementos a una lista: append() y insert()

"""  

Un elemento puede ser añadido al final de una lista existente:

list.append(value)

Dicha operación se reliza mediante un método llamado append().
El método append() agrega un elemento al final de la lista.

El método insert() permite agregar un elemento en una posición específica de la lista:

list.insert(location, value)

El método insert() recibe dos argumentos: la posición donde se desea insertar el 
elemento y el valor del elemento a insertar.
Si la posición es mayor que la longitud de la lista, el elemento se añadirá al final 
de la lista.

"""

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
numbers.insert(1, 333)
print(len(numbers))
print(numbers)

"""  

Se puede iniciar la vida de una lista con un elemento vacío, y luego ir agregando elementos:

"""

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)



lista = []  # Creando una lista vacía.

for i in range(5):
    lista.insert(0, i + 1)

print(lista)

