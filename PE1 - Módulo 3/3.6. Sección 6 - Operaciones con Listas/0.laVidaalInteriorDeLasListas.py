
#TODO Operaciones con Listas

#? La vida al interior de las listas

"""  

Las listas (y muchas otras entidades complejas de Python) se almacenan de diferentes maneras
que las variables ordinarias (escalares).

Se podría decir que:

- El nombre de una variable ordinaria es el nombre de su contenido.
- El nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

La asignación: list_2 = list_1 copia el nombre del arreglo no su contenido. En efecto, los
dos nombres (list_1 y list_2) apuntan a la misma lista en memoria. Modificar uno de ellos
afecta al otro, y viceversa.

"""

#? Rebanadas Poderosas (Powerful Slices)

"""  

Una rebanada (slice) es un elemento de la sintaxis de Python que permite hacer una copia
nueva de una lista, o partes de una lista.

En realidad, copia el contenido de la lista, no el nombre de la lista.

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

Su output es: [1]

Esta parte no visible del código descrito como [:] puede producir una lista completamente
nueva.

Esta nueva lista es independiente de la original. Si modificamos la nueva lista, la lista
original no se verá afectada.

Una de las formas más generales de la rebanada es:

my_list[inicio:fin]

Una rebanada de este tipo crea una nueva lista (de destino), tomando elementos de la lista
de origen - los elementos de los índices desde "inicio" hasta "fin - 1".

Nota: no hasta el fin sino hasta el índice "fin - 1". Un elemento con un indice igual a fin
es el primer elemento el cual no participa en la segmentación.

Es posible utilizar valores negativos tanto para el inicio como para el fin (al igual que
la indexación).

"""

# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
