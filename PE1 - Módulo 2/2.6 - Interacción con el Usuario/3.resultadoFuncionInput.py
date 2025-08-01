# El resultado de la función input() es el valor ingresado por el usuario.
# El resultado de la función input() es una cadena de texto (string).
# Si el usuario no ingresa nada y presiona Enter, el resultado será una cadena vacía.
# Si el usuario ingresa un valor, ese valor se convierte en una cadena de texto.
# La función input() no realiza ninguna conversión de tipo de dato, por lo que si se espera un número,
# Esto significa que no se debe utilizar como un argumento para operaciones matemáticas, por ejemplo, no se pueden utilizar estos datos para elevarlos al cuadrado, para dividirlos entre algo o por algo.


anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)

