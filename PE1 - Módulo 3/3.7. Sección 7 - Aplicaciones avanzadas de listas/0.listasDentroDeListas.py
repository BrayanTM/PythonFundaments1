
#TODO Sección 7 - Aplicaciones avanzadas de listas

#? Listas dentro de listas

"""  

Las listas pueden constar de escalares (es decir, números) y elementos de una estructura
mucho más compleja (cadenas, booleanos, listas).

A menudo encontraremos estos arreglos en nuestras vidas. Probablemente el mejor ejemplo
de esto sea un tablero de ajedrez.

Supongamos que podemos usar los números seleccionados para representar cualquier pieza 
de ajedrez. También podemos asumir que cada fila en el tablero de ajedrez es una lista.

Observa el siguiente código:

row = []
 
for i in range(8):
    row.append(WHITE_PAWN)

Crea una lista que contiene ocho elementos que representan la segunda fila del tablero de 
ajedrez: la que está llena de peones (supon que WHITE_PAWN es un símbolo predefinido que 
representa un peón blanco).
    
"""

#? Comprensión de Lista

"""  

El mismo efecto se puede lograr mediante una comprensión de lista, la sintaxis especial 
utilizada por Python para completar o llenar listas masivas.

Una comprensión de lista es en realidad una lista, pero se creó sobre la marcha durante 
la ejecución del programa, y no se describe de forma estática.

Echa un vistazo al fragmento:

row = [WHITE_PAWN for i in range(8)]
 
La parte del código colocada dentro de los paréntesis especifica:

- los datos que se utilizarán para completar la lista (WHITE_PAWN)
- la cláusula que especifica cuántas veces se producen los datos dentro de la lista (for 
  i in range(8))

"""

#* Ejemplo 1

squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""  

El fragmento de código genera una lista de diez elementos y la rellena con cuadrados de 
diez números enteros que comienzan desde cero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

"""

#* Ejemplo 2

twos = [2 ** i for i in range(8)]
print(twos)  # [1, 2, 4, 8, 16, 32, 64, 128]

"""  

El fragmento crea un arreglo de ocho elementos que contiene las primeras ocho potencias 
del numero dos (1, 2, 4, 8, 16, 32, 64, 128)

"""

#* Ejemplo 3

odds = [x for x in squares if x % 2 != 0 ]
print(odds)  # [1, 9, 25, 49, 81]

"""  

El fragmento crea una lista con solo los elementos impares de la lista squares.

"""