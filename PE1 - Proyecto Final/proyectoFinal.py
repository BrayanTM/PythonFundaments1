
#TODO Proyecto Final - Tic Tac Toe

from random import randrange

# Crear el tablero con números del 1 al 9, con X en la posición 5
board = []
num = 1
for i in range(3):
    row = []
    for j in range(3):
        if num == 5:
            row.append('X')
        else:
            row.append(str(num))
        num += 1
    board.append(row)

# Crea las fichas para jugar
system = "X"
user = "O"


def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.

    for row in range(3):
        # Línea superior
        print("+-------+-------+-------+")
        
        # Línea vacía superior
        print("|       |       |       |")
        
        # Línea con valores
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        
        # Línea vacía inferior
        print("|       |       |       |")
    
    # Línea final
    print("+-------+-------+-------+")


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        try:
            mov_user = int(input("Ingresa tu movimiento: "))
            if mov_user < 1 or mov_user > 9:
                print("Movimiento fuera de rango.")
                continue
        except ValueError:
            print("Entrada inválida, intenta de nuevo.")
            continue

    # aquí verificas casilla libre y haces el movimiento
        if mov_user < 4:
            if str(mov_user) in board[0]:
                board[0][mov_user-1] = user
                break
        elif mov_user < 7:
            if str(mov_user) in board[1]:
                board[1][mov_user-4] = user
                break
        elif mov_user < 10:
            if str(mov_user) in board[2]:
                board[2][mov_user-7] = user
                break
        print(f"El movimiento {mov_user} es invalido o ya esta ocupado, intentelo de nuevo!")


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    for i in range(3):
        if board[i] == [sign, sign, sign]:
            return True
        
    for i in range(3):
        col_comp = True
        for j in range(3):
            if board[j][i] != sign:
                col_comp = False
                break
        if col_comp:
            return True

    row_comp1 = True    
    for i in range(3):
        if board[i][i] != sign:
            row_comp1 = False
            break
    if row_comp1:
        return True

    row_comp2 = True
    for i in range(3):
        if board[i][2-i] != sign:
            row_comp2 = False
            break
    if row_comp2:
        return True

    return False


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free_fields = make_list_of_free_fields(board)
    for i in range(len(free_fields)):
        num_tuple = i + 1
    val = randrange(num_tuple)

    tup_sel = list(free_fields[val])

    x = tup_sel[0]
    y = tup_sel[1]

    board[x][y] = system

# Mostrar el tablero
display_board(board)
while True:
    #El usuario ingresa su movimiento
    enter_move(board)
    display_board(board)

    # Verificar si el usuario ha ganado
    if victory_for(board, "O"):
        display_board(board)
        print("Has Ganado!!")
        break
    elif victory_for(board, "X"):
        display_board(board)
        print("La Computadora Ha Ganado!!")
        break
    elif not make_list_of_free_fields(board):
        display_board(board)
        print("Empate!!")
        break

    # La computadora hace su movimiento
    draw_move(board)
    display_board(board)

    # Verificar si el usuario ha ganado
    if victory_for(board, "O"):
        display_board(board)
        print("Has Ganado!!")
        break
    elif victory_for(board, "X"):
        display_board(board)
        print("La Computadora Ha Ganado!!")
        break
    elif not make_list_of_free_fields(board):
        display_board(board)
        print("Empate!!")
        break