# Variables en Python
# Definición de variables
# Las variables son contenedores que almacenan datos.
# En Python, no es necesario declarar el tipo de variable.

var = 1
account_balance = 1000.0
client_name = "Brayan"
print(var, account_balance, client_name)
print(var)

# Errores comunes al definir variables
# 1. No se pueden iniciar con un número.
# 2. No se pueden usar caracteres especiales (excepto guiones bajos).
# 3. No se pueden usar palabras reservadas de Python.

# Ejemplos de errores comunes
# 1. 1var = 5  # Error: no puede iniciar con un número
# 2. var@name = "Brayan"  # Error: no se permiten caracteres especiales
# 3. def = "función"  # Error: 'def' es una palabra reservada

# var = 1
# print(Var)

# Corrección del error
# En Python, las variables son sensibles a mayúsculas y minúsculas.
# Por lo tanto, 'var' y 'Var' son dos variables diferentes.

var = 1
print(var)  # Imprime el valor de la variable 'var'

# Se puede utilizar print() para combinar texto y variables utilizando el operador de concatenación (+)

version = "3.8.5"
print("La versión de Python es: " + version)

# Asignar un nuevo valor a una variable ya definida
# Esto es útil cuando se necesita actualizar el valor de una variable.

var = 2
print(var)  # Imprime el nuevo valor de la variable 'var'
var = var + 1
print(var)  # Imprime el valor actualizado de la variable 'var'

