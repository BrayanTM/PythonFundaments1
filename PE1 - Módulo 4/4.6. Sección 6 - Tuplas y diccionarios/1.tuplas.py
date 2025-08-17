
#TODO Tuplas

"""  

Lo primero que distingue una lista de una tupla es la sintaxis empleada para crearlas - las 
tuplas utilizan paréntesis, mientras que las listas usan corchetes, aunque también es posible 
crear una tupla tan solo separando los valores por comas.

"""

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

#? ¿Cómo crear una tupla?

"""  

Es posible crear una tupla vacía? Si, se puede hacer de la siguiente manera:

"""

empty_tuple = ()

print(empty_tuple)

"""  

Se puede crear una tupla de un solo elemento? Si, pero es necesario incluir una coma después 
del elemento:

"""

single_element_tuple = (1,)
single_element_tuple2 = 1,

print(single_element_tuple)
print(single_element_tuple2)
print("")

#? ¿Cómo utilizar una tupla?

"""  

Las tuplas se pueden utilizar de manera similar a las listas, pero son inmutables. Esto significa 
que no se pueden modificar una vez creadas. Por ejemplo, no se pueden agregar, eliminar o cambiar 
elementos en una tupla.

"""

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
print("")

#? ¿Qué más pueden hacer las tuplas?

"""  

- la función len() acepta tuplas, y regresa el número de elementos contenidos dentro;
- el operador + puede unir tuplas (ya se ha mostrado esto antes)
- el operador * puede multiplicar las tuplas, así como las listas;
- los operadores in y not in funcionan de la misma manera que en las listas.

"""

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
print("")

"""  

Una de las propiedades de las tuplas más útiles es que pueden aparecer en el lado izquierdo 
del operador de asignación. Este fenómeno ya se vio con anterioridad, cuando fue necesario 
encontrar una manera de intercambiar los valores entre dos variables.

"""

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

"""  

Muestra tres tuplas interactuando - en efecto, los valores almacenados en ellas "circulan" entre 
ellas - t1 se convierte en t2, t2 se convierte en t3, y t3 se convierte en t1.

Nota: el ejemplo presenta un importante hecho mas: los elementos de una tupla pueden ser variables, 
no solo literales. Además, pueden ser expresiones si se encuentran en el lado derecho del operador 
de asignación.

"""