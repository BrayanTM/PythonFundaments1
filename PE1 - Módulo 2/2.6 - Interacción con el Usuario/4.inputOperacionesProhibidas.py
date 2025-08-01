# Funcion Input - Operaciones Prohibidas
# La función input() devuelve una cadena de texto (string), por lo que no se pueden realizar operaciones matemáticas directamente con su resultado.
# Si se necesita realizar operaciones matemáticas, es necesario convertir la cadena a un tipo numérico.

anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)
# Esto generará un error porque anything es una cadena de texto, no un número.

