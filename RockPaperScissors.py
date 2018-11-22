#Welcome to Paper, Scissors and Rock! -- Done
#Would you like to play? -- Done
#Instituted a game switch known as playing.
#If playing, run the code that goes through the logic of the game
#Please select (P)aper, (S)cissors, or (R)ock!
#User selects (P)
#They either Win, lose, or tie.
#Would you like to play again? Y or N?
import random
print('Welcome to Paper, Scissors and Rock!')

playerInput = input('Would you like to play? Y or N?')

if playerInput[0].lower() == 'y':
    #turn the switch on, baby
    playing = True
else:
    print('Sweet, I didnt want to play with you anyway!')
    playing = False

while playing == True:
    moves = ['Paper','Scissors','Rock']

    randomInteger = random.randint(0,2)

    computerMove = moves[randomInteger]


    playerMove = input('Please pick [P]aper, [S]cissors or [R]ock! ')

    if playerMove.lower() == 'p':
        playerMove = moves[0] #Paper 
    elif playerMove.lower() == 's':
        playerMove = moves[1] #Scissor
    else:
        playerMove = moves[2] #Rock
    

    #if the player chose PAPER
    if playerMove == moves[0] and computerMove == moves[0]:
        print('It is a tie, you both chose Paper!')
    elif playerMove == moves[0] and computerMove == moves[1]: #Paper v Scissor
        print('Player lost, Scissors cuts Paper')
    elif playerMove == moves[0] and computerMove == moves[2]: #Paper v Rock
        print('You win! Paper covers Rock')
    
    #if the player chose SCISSOR
    elif playerMove == moves[1] and computerMove == moves[0]: #Scissor v Paper
        print('You win! Scissor cuts Paper')
    elif playerMove == moves[1] and computerMove == moves[1]: #Scissor v Scissor
        print('It is a tie, you both chose Scissor!')
    elif playerMove == moves[1] and computerMove == moves[1]: #Scissor v Rock
        print('Player lost, Rock smashes Scissor')
    
    #if the player chose ROCK
    elif playerMove == moves[2] and computerMove == moves[0]: #Rock v Paper
        print('Player lost, Paper covers Rock')
    elif playerMove == moves[2] and computerMove == moves[1]: #Rock v Scissor
        print('You win! Rock smashes Scissor')
    elif playerMove == moves[2] and computerMove == moves[2]: #Rock v Rock
        print('It is a tie, you both chose Rock!')