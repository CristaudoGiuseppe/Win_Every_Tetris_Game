#turn 1

board = {   1 : " ", 2 : " ", 3 : " ",
            4 : " ", 5 : " ", 6 : " ",
            7 : " ", 8 : " ", 9 : " "}

def print_board():
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("\n\n")

"""
def is_space_free(position):
    if board[position] == ' ':
        return True
    else:
        return False
""" # used for minmax alghoritm testing

def check_draw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def check_goal_state():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
    
def check_player_win(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def write_board(player, position):
    #if is_space_free(position):
    board[position] = player
    print_board()
    if check_goal_state():
        if player == 'X':
            print("X win")
        else:
            print("O win")
    if check_draw():
        print("Draw")
    return  
    """"
    else:
        print("Space " + str(position)  + " is already used!")
        p = int(input("Enter a new position: "))
        write_board('O', p)
        return
    """

def human_move():
    best_score = 1000
    best_move = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'O'
            score = minmax(board, 0, True)
            board[key] = ' '
            if score < best_score:
                best_score = score
                best_move = key
    print("O moves in " + str(best_move))
    write_board('O', best_move)
    return

def bot_move():
    best_score = -1000
    best_move = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            score = minmax(board, 0, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    print("X moves in " + str(best_move))
    write_board('X', best_move)

def minmax(board, depth, isMax):
    if check_player_win('X'):
        return 100
    elif check_player_win('O'):
        return -100
    elif check_draw():
        return 0
    
    if isMax:
        best_score = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minmax(board, 0, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score

        return best_score
    else:
        best_score = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minmax(board, 0, True)
                board[key] = ' '
                if score < best_score:
                    best_score = score

        return best_score

def count_X_and_O(board):
    n_X = 0
    n_O = 0  
    for key in board.keys():
        if board.get(key) == 'X':
            n_X += 1
        if board.get(key) == 'O':
            n_O += 1
    return n_X, n_O  

def load_board(symbols):
    for i in range(0, len(symbols)):
        if symbols[i] != 'empty':
            board[i+1] = symbols[i]
    
    print(board)
    print(count_X_and_O(board))
    n_X, n_O  = count_X_and_O(board)

    if n_X <= n_O:
        bot_move()
    else:
        human_move()