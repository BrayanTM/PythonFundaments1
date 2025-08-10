
#TODO Arreglos de Dos Dimensiones

"""  

Los arreglos de dos dimensiones son simplemente listas de listas. Esto significa que
podemos tener una lista que contenga otras listas como elementos. Este tipo de estructura
es útil para representar datos en forma de tabla, como una hoja de cálculo o una matriz.

Supongamos también que un símbolo predefinido denominado EMPTY designa un campo vacío en 
el tablero de ajedrez.

Entonces, si queremos crear una lista de listas que representan todo el tablero de ajedrez, 
se puede hacer de la siguiente manera:

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

Nota:

- la parte interior del bucle crea una fila que consta de ocho elementos (cada uno de ellos 
  es igual a EMPTY) y lo agrega a la lista del board;
- la parte exterior se repite ocho veces;
- en total, la lista board consta de 64 elementos (todos iguales a EMPTY).

Como las listas de comprensión puedes ser anidadas, podemos acortar la creación del tablero
de la siguiente manera:

board = [[EMPTY for i in range(8)] for j in range(8)]

"""

board = [["EMPTY" for i in range(8)] for j in range(8)]

print(len(board))
print(board)

board[0][7] = "ROOK"
board[0][0] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"

board[4][2] = "KNIGHT"

board[3][4] = "PAWN"

print(board)

"""  
Salida:

[['ROOK', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'ROOK'], 
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'], 
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'], 
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'PAWN', 'EMPTY', 'EMPTY', 'EMPTY'], 
['EMPTY', 'EMPTY', 'KNIGHT', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'], 
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'], 
['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'], 
['ROOK', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'ROOK']]

"""