
#TODO Rebanadas - Indices Negativos

"""  

Observa el código a continuación:

my_list[start:end]

Para confirmar:
- start es el índice del primer elemento incluido en la rebanada.
- end es el índice del primer elemento no incluido en la rebanada.

Así es como los índices negativos funcionan en las rebanadas:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

El resultado es: [8, 6, 4]

Si start especifica un elemento que se encuentra más allá del descrito por end (desde el punto
de vista inicial de la lista), la rebanada estará vacía:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

La output del fragmento es: []

Si omites el start en tu rebanada, se supone que deseas obtener un segundo elemento que 
comienza en el elemento con índice 0.

En otras palabras, la rebanada sería de esta forma:

my_list[:end]

es un equivalente más compacto de:

my_list[0:end]

Observa el fragmento de código a continuación:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

El resultado es: [10, 8, 6]

Del mismo modo, si omites el end en tu rebanada, se supone que deseas que el segmento termine
con el índice len(my_list).

En otras palabras, la rebanada sería de esta forma:

my_list[start:]

Es un equivalente más compacto de:

my_list[start:len(my_list)]

Observa el fragmento de código a continuación:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

El resultado es: [4, 2]

Como se ha dicho anteriormente, el omitir el inicio y fin crea una copia de toda la lista:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

El resultado es: [10, 8, 6, 4, 2]

"""

#? Más sobre la instrucción del

"""  

La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a
la vez - también puede eliminar rebanadas.

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

Nota: En este caso, la rebanada !No produce ninguna lista nueva!

El resultado es: [10, 4, 2]

También es posible eliminar todos los elementos a la vez:

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

El resultado es: []

Al eliminar la rebanada del código, su significado cambia dramáticamente.

Echa un vistazo:

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)

La instrucción del eliminará la lista, no su contenido.

La función print() de la última línea de código provocará un error de ejecución.

"""

#? Los operadores in y not in

"""  

Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar 
si un valor específico está almacenado dentro de la lista o no.

elem in my_list
elem not in my_list

El primero de ellos (in) verifica si un elemento dado (el argumento izquierdo) está 
actualmente almacenado en algún lugar dentro de la lista (el argumento derecho) - el 
operador devuelve True en este caso.

El segundo (not in) comprueba si un elemento dado (el argumento izquierdo) está ausente 
en una lista - el operador devuelve True en este caso.

"""

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

