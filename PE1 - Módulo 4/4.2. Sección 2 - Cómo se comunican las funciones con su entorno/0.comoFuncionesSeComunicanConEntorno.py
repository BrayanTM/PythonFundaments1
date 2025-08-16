
#TODO Cómo las funciones se comunican con su entorno.

#? Funciones Parametrizadas

"""  

Un parámetro en una variable, pero existen dos factores que hacen a un parámetro diferente:
- los parámetros solo existen dentro de las funciones en donde han sido definidos, y el único 
  lugar donde un parámetro puede ser definido es entre los paréntesis después del nombre de la 
  función, donde se encuentra la palabra clave reservada def;
- la asignación de un valor a un parámetro de una función se hace en el momento en que la función 
  se manda llamar o se invoca, especificando el argumento correspondiente.

def function(parameter):
    ###

Recuerda que:

- los parámetros solo existen dentro de las funciones (este es su entorno natural)
- los argumentos existen fuera de las funciones, y son los que pasan los valores a los parámetros 
  correspondientes.
  
Una función puede tener tantos parámetros como se desee, pero entre más parámetros, es más dificil
memorizar su rol y propósito.

def message(what, number):
    print("Ingresa", what, "número", number)

Esto significa que para invocar la función se necesitan dos argumentos.

El primer parámetro va a contener el nombre del valor deseado.
El segundo parámetro va a contener el número del valor deseado.

"""

def message(what, number):
    print("Ingresa", what, "número", number)

message("teléfono", 11)
message("precio", 5)
message("número", "number")
print("")

#? Paso de parámetros posicionales

"""  

La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros 
posicionales, los argumentos pasados de esta manera son llamados argumentos posicionales.

def my_function(a, b, c):
    print(a, b, c)
 
my_function(1, 2, 3)

"""

#? Paso de argumentos de palabra clave

"""

Python ofrece otra manera de pasar argumentos, donde el significado del argumento está definido 
por su nombre, no su posición - a esto se le denomina paso de argumentos con palabra clave.

Observa el siguiente código:

"""

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
print("")

#? Mezclando Argumentos Posicionales y de Palabras Clave

"""  

Es posible combinar ambos tipos si se desea - solo hay una regla inquebrantable: se deben colocar 
primero los argumentos posicionales y después los de palabra clave.

"""

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c) #Su propósito es el de evaluar y presentar la suma de todos sus argumentos.

adding(1, 2, 3) # Llamada con argumentos posicionales
adding(c = 1, a = 2, b = 3) # Llamada con argumentos de palabra clave
adding(3, c = 1, b = 2) # Llamada mixta
print("")


#? Funciones Parametrizadas - Más Detalles

"""  

En ocasiones ocurre que algunos valores de ciertos argumentos son más utilizados que otros. Dichos 
argumentos tienen valores predefinidos los cuales pueden ser considerados cuando los argumentos 
correspondientes han sido omitidos.

El valor por predeterminada para el parámetro se asigna de la siguiente manera:

"""

def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)

introduction("Jorge", "Pérez")
introduction("Enrique")
introduction(first_name="Guillermo")
print("")

"""  

Puedes hacerlo con más parámetros, si te resulta útil. Ambos parámetros tendrán sus valores por 
predeterminada, observa el siguiente código:

"""

def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction()
introduction(last_name="Rodríguez")


