import random
def display_board(board):
    print('\n'*100)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

def player_input():
    marker = "" #starting marker off at no value
    while marker.lower() != 'o' and marker.lower() != 'x':
        marker = input('Player1, please choose your symbol: X or O? ').upper() #repeatedly ask when its neither o or x
    if marker.lower() == 'x':
        return ("X","O")
    else:
        return ("O","X")

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    
    return (board[2] == board[5] == board[9] == mark or #Diagonal going down
    board[3] == board[5] == board[7] == mark or #diagonal going up left to right
    board[1] == board[2] == board[3] == mark or #across top
    board[4] == board[5] == board[6] == mark or #across the middle
    board[7] == board[8] == board[9] == mark or #across the bottom
    board[1] == board[4] == board[7] == mark or #down the left
    board[2] == board[5] == board[8] == mark or #down the middle
    board[3] == board[6] == board[9] == mark) #down the right

def choose_first():
    flip = random.randint(0,1) #Is it random.randint(0,1)?
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    return board[position] == ' ' #True if available, False if not

def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i): #running space check for every position in the board
            return False #return False if unavailable
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("choose a position 1-9: "))
    return position

def replay():
    playerchoice = input("Do you want to play again? Yes or No?")
    
    if playerchoice.startswith( 'y' ) or  playerchoice.startswith( 'Y' ):
        return True
    else:
        return False

import random
print('Welcome to Tic Tac Toe!')

while True: #To keep running the game
    # Set the game up here
    the_board = [' ']*10 #setting up an empty board 
    player1marker, player2marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? y or n?')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    #pass

    while game_on:
        
        if turn == 'Player 1':
            
            display_board(the_board) #board display
            position = player_choice(the_board) #choosing a position
            place_marker(the_board,player1marker,position)
            if win_check(the_board,player1marker):
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board) #board display
            position = player_choice(the_board) #choosing a position
            place_marker(the_board,player2marker,position)
            if win_check(the_board,player2marker):
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break