#                                              F U N C T I O N S
# board
# display board
# play game
# handle turn
# check win
#     check rows
#     check columns
#     check diagonals
# check tie
# flip player

#                                                  B U I L D 

board = ['_','_','_',
         '_','_','_',
         '_','_','_',]

game_still_going = True

winner = None

current_player = 'X'


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")

def play_game():

    display_board()

    while game_still_going:
        
        handle_turn(current_player)

        check_if_gameover()

        flip_player()
    
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')

    elif winner == None:
        print('Tie.')


def handle_turn(player):
    print(player + "'s turn" )
    position = input('Choose your position from 1-9: ')

    valid = False
    while not valid:
        
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Choose your position from 1-9: ')


        position = int(position) - 1

        if board[position] == '_':
            valid = True

        else:
            print("You can't go there. Go again")

    board[position] = player

    display_board()


def check_if_gameover():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diag_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diag_winner:
        winner = diag_winner

    else:
        winner = None


def check_rows():

    global game_still_going

    row1 = board[0] == board[1] == board[2] != '_'
    row2 = board[3] == board[4] == board[5] != '_'
    row3 = board[6] == board[7] == board[8] != '_'

    if row1 or row2 or row3:
        game_still_going = False
    
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_columns():

    global game_still_going

    col1 = board[0] == board[3] == board[6] != '_'
    col2 = board[1] == board[4] == board[7] != '_'
    col3 = board[2] == board[5] == board[8] != '_'

    if col1 or col2 or col3:
        game_still_going = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[3]
    
    else:
        return None


def check_diagonals():
    
    global game_still_going

    diag1 = board[0] == board[4] == board[8] != '_'
    diag2 = board[2] == board[4] == board[6] != '_'
    
    if diag1 or diag2:
        game_still_going = False

    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    
    else:
        return None 


def check_if_tie():

    global game_still_going

    if '_' not in board:
        game_still_going = False
        return True

    else:
        return False


def flip_player():

    global current_player

    if current_player == 'X':
        current_player = 'O'
    
    elif current_player == 'O':
        current_player = 'X'


play_game()