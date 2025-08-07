
#TODO Listas en Python

#? Por que necesitamos listas?

"""  

Las listas son una estructura de datos que nos permite almacenar múltiples 
elementos en una sola variable.
Son útiles cuando necesitamos agrupar datos relacionados, como una lista de 
nombres, números o cualquier otro tipo de información.

Las listas son mutables, lo que significa que podemos modificar su contenido
después de haberlas creado. Esto nos permite agregar, eliminar o cambiar 
elementos en la lista según sea necesario.

Las listas son versátiles y se pueden utilizar en una amplia variedad de 
aplicaciones, desde almacenar datos temporales hasta representar colecciones 
de objetos más complejos.

En resumen, las listas son una herramienta fundamental en Python que nos 
permite trabajar con conjuntos de datos de manera eficiente y flexible.

"""

#? Indexación de listas

"""  

Las listas en Python son indexadas, lo que significa que cada elemento de la
lista tiene un índice asociado que comienza en 0. Esto nos permite acceder a 
los elementos de la lista utilizando su índice.

Cómo cambiar el valor de un elemento en una lista?

"""

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers) # Imprimendo el contenido de la lista

numbers[0] = 111
print("Nuevo contenido de la lista:", numbers) # Imprimiendo el nuevo contenido de la lista

# y ahora queremos copiar el valor del quinto elemento al segundo elemento

numbers[1] = numbers[4]
print("Contenido de la lista después de la copia:", numbers) # Imprimiendo el contenido de la lista después de la copia

"""  

El valor dentro de los corchetes que selecciona un elemento de la lista se llama 
un índice, mientras que la operación de seleccionar un elemento de la lista se 
conoce como indexación.

Nota: todos los índices utilizados hasta ahora son literales. Sus valores se fijan 
en el tiempo de ejecución, pero cualquier expresión también puede ser un índice. 
Esto abre muchas posibilidades.

"""
