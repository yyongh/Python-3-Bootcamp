# functions used
# print board
def display_board(board):
    print("Here is the current board: ")
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print("——— ——— ———")
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print("——— ——— ———")
    print(f' {board[7]} | {board[8]} | {board[9]} ')

# player chooses to be X or O
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, would you like to be X or O?").upper()
        if marker not in ['X','O']:
            print("Sorry that is not accepted!")
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

# put X or O on board
def place_marker(board, marker, position):
    board[position] = marker

# check winning patterns
def win_check(board, mark):
    return (
    (board[1] == mark and board[2] == mark and board[3] == mark) #row1
    or (board[4] == mark and board[5] == mark and board[6] == mark) #row2
    or (board[7] == mark and board[8] == mark and board[9] == mark) #row3
    or (board[1] == mark and board[4] == mark and board[7] == mark) #col1
    or (board[2] == mark and board[5] == mark and board[8] == mark) #col2
    or (board[3] == mark and board[6] == mark and board[9] == mark) #col3
    or (board[1] == mark and board[5] == mark and board[9] == mark) #dia1
    or (board[3] == mark and board[5] == mark and board[7] == mark) #dia2
    )

# which player goes first
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# check if position is empty
def space_check(board, position):
    return board[position] not in ['X','O']

# check if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False #empty position, board is NOT full
    return True

# pick position
def player_choice(board):
    choice = 0
    
    while choice not in range(1,11) or space_check(board,choice) == False:
        choice = input('Pick a spot: ')
        if choice.isdigit():
            if int(choice) in range(1,11):
                choice = int(choice)
                if space_check(board,choice) == False:
                    print("That spot is taken!")
            else:
                print("Sorry that is not accepted!")            
        else:
            print("Sorry that is not accepted!")

    return choice

# play again
def replay():
    choice = 'WRONG'
    
    while choice not in ['Y','N']:
        choice = input("Keep playing? (Y/N): ").upper()
        if choice not in ['Y','N']:
            print("Sorry that is not accepted!")
    if choice == 'Y':
        return True
    else:
        print("Thanks for playing!")
        return False


# game starts here
from IPython.display import clear_output

print('Welcome to Tic Tac Toe!')

while True:
    game_board = ['#','1','2','3','4','5','6','7','8','9']
    player1_marker, player2_marker = player_input()
    
    clear_output()
    turn = choose_first()
    print(turn + " will go first.")

    play_game = ''    
    while play_game not in ['Y','N']:
        play_game = input("Are you ready to play? (Y/N)").upper()
        if play_game not in ['Y','N']:
            print("Sorry that is not accepted!")
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1 Turn
        if turn == 'Player 1':
            clear_output()
            display_board(game_board)
            print(f'Your turn, Player 1. Place your "{player1_marker}".')
            position = player_choice(game_board)
            place_marker(game_board, player1_marker, position)
            
            if win_check(game_board,player1_marker):
                clear_output()
                display_board(game_board)
                print("You win!")
                game_on = False
            else:
                if full_board_check(game_board):
                    clear_output()
                    display_board(game_board)
                    print("It's a draw!")
                    game_on = False
                else:
                    turn = 'Player 2'
        
        # Player2's turn
        else:
            clear_output()
            display_board(game_board)
            print(f'Your turn, Player 2. Place your "{player2_marker}".')
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)
            
            if win_check(game_board,player2_marker):
                clear_output()
                display_board(game_board)
                print("You win!")
                game_on = False
            else:
                if full_board_check(game_board):
                    clear_output()
                    display_board(game_board)
                    print("It's a draw!")
                    game_on = False
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break
