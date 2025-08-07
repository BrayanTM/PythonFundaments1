
#TODO Eliminando elementos de una lista

"""  

Cualquier elemento de la lista puede ser eliminado en cualquier momento - esto
se hace con una instrucción llamada del (eliminar). Nota: es una intrucción,
no una función, por lo que no utiliza paréntesis.

"""

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

###

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

###

print(numbers[4])
numbers[4] = 1

"""  

Nota: hemos eliminado uno de los elementos de la lista - ahora solo hay cuatro 
elementos en la lista. Esto significa que el elemento número cuatro no existe.

"""