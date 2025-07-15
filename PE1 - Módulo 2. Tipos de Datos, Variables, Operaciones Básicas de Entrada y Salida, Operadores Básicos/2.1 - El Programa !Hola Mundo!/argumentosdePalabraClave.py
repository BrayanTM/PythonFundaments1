# Ejemplo de uso de argumentos de palabra clave en print
# end es un argumento de palabra clave que permite especificar qué se imprime al final de la línea

print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

# El argumento end permite cambiar el final de la línea
print("Mi nombre es ", end="")
print("Monty Python.")

# También se puede usar sep para especificar el separador entre los argumentos
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

# Se pueden combinar ambos argumentos de palabra clave 
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

