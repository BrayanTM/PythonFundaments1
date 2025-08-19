
#TODO Diccionarios

"""  

Los diccionarios son estructuras de datos que permiten almacenar pares de clave-valor. A diferencia 
de las listas y tuplas, los diccionarios no tienen un orden específico y se accede a sus elementos 
mediante claves en lugar de índices.

"""

#? ¿Cómo crear un diccionario?

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

"""  

En el mundo de Python, la palabra que se esta buscando se denomina key. La palabra que se obtiene del 
diccionario es denominada value.

Esto significa que un diccionario es un conjunto de pares de key y value. Nota:

- cada clave debe de ser única - no es posible tener una clave duplicada;
- una clave puede ser un de dato de cualquier tipo - puede ser un número (entero o flotante), incluso 
  una cadena, pero no una lista;
- un diccionario no es una lista - una lista contiene un conjunto de valores numerados, mientras que 
  un diccionario almacena pares de valores;
- la función len() aplica también para los diccionarios - regresa la cantidad de pares (clave-valor) 
  en el diccionario;
- un diccionario es una herramienta de un solo sentido - si fuese un diccionario español-francés, 
  podríamos buscar en español para encontrar su contraparte en francés más no viceversa.

"""

#? ¿Cómo utilizar un diccionario?

"""  

Para acceder a un valor en un diccionario, se utiliza la clave correspondiente entre corchetes.

"""

print(dictionary["gato"])  # Imprime "chat"
print(phone_numbers["jefe"])  # Imprime 5551234567
print("")

"""  

El obtener el valor de un diccionario es semejante a la indexación, gracias a los corchetes alrededor 
del valor de la clave.

Nota:

- si una clave es una cadena, se tiene que especificar como una cadena;
- las claves son sensibles a las mayúsculas y minúsculas: 'Suzy' sería diferente a 'suzy'.

Ahora algo muy importante: No se puede utilizar una clave que no exista
Afortunadamente, existe una manera simple de evitar dicha situación. El operador in, junto 
con su acompañante, not in, pueden salvarnos de esta situación.

El siguiente código busca de manera segura palabras en francés:

"""

#dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
print("")


"""  

Cuando escribes una expresión grande o larga, puede ser una buena idea mantenerla alineada 
verticalmente. Así es como puede hacer que el código sea más legible y más amigable para el 
programador, por ejemplo:

"""

# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
              'Suzy': 22657854310
}

