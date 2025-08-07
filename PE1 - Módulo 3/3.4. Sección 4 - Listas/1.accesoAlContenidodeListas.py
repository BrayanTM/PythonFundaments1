
#TODO Acceso al contenido de las listas

""" 

Se puede acceder a cada uno de los elementos de la lista por separado. 
Por ejemplo, se puede imprimir:

print(numbers[0])  # Imprime el primer elemento de la lista

"""

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.


#? La función len().

"""  

La función len() devuelve la cantidad de elementos que tiene una lista.
Por ejemplo, si tenemos una lista llamada "numbers", podemos obtener su longitud con:

print(len(numbers))  # Imprime la cantidad de elementos en la lista numbers

"""