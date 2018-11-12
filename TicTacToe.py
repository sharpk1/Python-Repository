

board = ['1','2','3','4','5','6','7','8','9']
def printBoard():
        print(board[0] +'|'+ board[1] +'|'+ board[2])
        print(board[3] +'|'+ board[4] +'|'+ board[5])
        print(board[6] +'|'+ board[7] +'|'+ board[8])

# def boardChecker(): #This needs some heavy work to be done on
        # gameSwitch = True #gameSwitch is True if the game is still going on

        # while gameSwitch == True:
        #         if board[0] == "X" and player1.lower() == 'x':
        #                 print("Player 1 has won the game.")
        #                 #Figure out what does it do once we hit these X's
        #                 #Must we create another method that will take us out and end the game?
        #                 #Whats the most dynamic way to end the game?
        #                 #We need it to not ask the Player's move
        #                 #and it also should not show the board?
        #                 #it will make the gameSwitch to false but it will still ask for Player 2's turn
        #                 break
        #                 #gameSwitch = False
        #         # else:
        #         #         pass
        #         while gameSwitch == False:
        #                 print('the game is complete')
        #                 break
        
        # if board[0] == "X" and board[1] == "X" and board[2] == "X":
        #         print("This shit is working")
        #         print('Player X wins!')

def boardChanger(player1):
        #The point of this method is to switch between player 1 and player 2 via the PlayerSwitch variable

        playerSwitch = True #Acts as a switch to indicate whether its Player1's turn(True) or Player2's turn(False)
        playerOneInput = 0
        playerTwoInput = 0

        while playerSwitch == True:
                print('We are on Player 1s turn')
                printBoard()
                playerOneInput = input('Player 1, please select a number: ')
                if playerOneInput == '1' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console
                        board[0] = "X"
                        # boardChecker()
                        
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                        
                elif playerOneInput == '2' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console 
                        board[1] = "X"
                        #boardChecker()
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                        
                elif playerOneInput == '3' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console 
                        board[2] = "X"
                        #boardChecker()
                        print('Player 1s move has been made. Switching now to Player 2')
                        
                        playerSwitch = False
                        
                elif playerOneInput == '4' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console 
                        board[3] = "X"
                        #boardChecker()
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '5' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console 
                        board[4] = "X"
                        #boardChecker()
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '6' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console 
                        board[5] = "X"
                        #boardChecker()
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '7' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console 
                        board[6] = "X"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '8' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console 
                        board[7] = "X"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '9' and player1.lower() == 'x':
                        print('\n'*100) #Clears the console 
                        board[8] = "X"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                #Adding if Player 1 == O
                elif playerOneInput == '1' and player1.lower() == 'o':
                        print('\n'*100) #Clears the console 
                        board[0] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '2' and player1.lower() == 'o':
                        board[1] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '3' and player1.lower() == 'o':
                        board[2] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '4' and player1.lower() == 'o':
                        board[3] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '5' and player1.lower() == 'o':
                        board[4] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '6' and player1.lower() == 'o':
                        board[5] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '7' and player1.lower() == 'o':
                        board[6] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '8' and player1.lower() == 'o':
                        board[7] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                elif playerOneInput == '9' and player1.lower() == 'o':
                        board[8] = "O"
                        print('Player 1s move has been made. Switching now to Player 2')
                        playerSwitch = False
                #End of if Player 1 == O
                elif playerOneInput == 'q': #This acts as a Killswitch for the game
                        break
                while playerSwitch == False:
                        print('We are on Player 2s turn')
                        printBoard()
                        
                        playerTwoInput = input('Player 2, please select a number:  ')
                        #Below this needs to be removed
                        # if playerTwoInput == 's':
                        #         print('Player 2s move has been made. Switching now to Player 1')
                        #         playerSwitch = True
                        # elif playerTwoInput == 'q':
                        #         break
                        #Being added after this line
                        if playerTwoInput == '1' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[0] = "O"
                                #boardChecker()
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '2' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[1] = "O"
                                #boardChecker()
                                print('Player 2s move has been made. Switching now to Player 2')
                                playerSwitch = True
                        elif playerTwoInput == '3' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[2] = "O"
                                #boardChecker()
                                print('Player 2s move has been made. Switching now to Player 2')
                                playerSwitch = True
                        elif playerTwoInput == '4' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[3] = "O"
                                #boardChecker()
                                print('Player 2s move has been made. Switching now to Player 2')
                                playerSwitch = True
                        elif playerTwoInput == '5' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[4] = "O"
                                print('Player 2s move has been made. Switching now to Player 2')
                                playerSwitch = True
                        elif playerTwoInput == '6' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[5] = "O"
                                print('Player 2s move has been made. Switching now to Player 2')
                                playerSwitch = True
                        elif playerTwoInput == '7' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[6] = "O"
                                print('Player 2s move has been made. Switching now to Player 2')
                                playerSwitch = True
                        elif playerTwoInput == '8' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[7] = "O"
                                print('Player 2s move has been made. Switching now to Player 2')
                                playerSwitch = True
                        elif playerTwoInput == '9' and player2.lower() == 'o':
                                print('\n'*100) #Clears the console 
                                board[8] = "O"
                                print('Player 2s move has been made. Switching now to Player 2')
                                playerSwitch = True
                        #Adding if Player 2 is X
                        elif playerTwoInput == '1' and player2.lower() == 'x':
                                print('\n'*100) #Clears the console 
                                board[0] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '2' and player2.lower() == 'x':
                                board[1] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '3' and player2.lower() == 'x':
                                board[2] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '4' and player2.lower() == 'x':
                                board[3] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '5' and player2.lower() == 'x':
                                board[4] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '6' and player2.lower() == 'x':
                                board[5] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '7' and player2.lower() == 'x':
                                board[6] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '8' and player2.lower() == 'x':
                                board[7] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        elif playerTwoInput == '9' and player2.lower() == 'x':
                                board[8] = "X"
                                print('Player 2s move has been made. Switching now to Player 1')
                                playerSwitch = True
                        #End of Player 2 being X
                        elif playerTwoInput == 'q':
                                break #This acts as a killswitch for the game

def playerAssignment():
        #The purpose of this method is to assign Player 1 and Player 2 either X or O. 
        marker = '' #Empty string for marker to be set to X or O
        while marker.lower() != 'x' and marker.lower() != 'o': #While loop to make sure Player 1 inputs X or O
                marker = input("Player 1, choose X or O: ") #Setting marker to X or O
                player1 = marker
        if player1.lower() == 'x': #hit X
                player2 = 'o' #assigned player2 as o
                print('Player 1 is now {} and Player 2 is now {}'.format(player1.upper(),player2.upper()))                
        else:
                player2 = 'x'
                print('Player 1 is now {} and Player 2 is now {}'.format(player1.upper(),player2.upper()))
        return (player1,player2)

player1,player2 = playerAssignment()
boardChanger(player1)







#Action Items:
#       3. Have the console clear whenever a move is made -- DONE
#               A. Definitely clean up some of the shit that gets printed -- DONE
#       3.5. Need to take into account if Player 1 is O and Player 2 is X. -- DONE
#       4. There must be a checker method in which the board will be scanned -- NOT DONE
#               A. Two outcomes ought to occur: Tie or Win -- NOT DONE
#                       I. if Board[0], Board[1], and Board[2] == X (ACROSS TOP)
#                       II. if Board[3], Board[4], and Board[5] == X (ACROSS MIDDLE)
#                       III. if Board[6], Board[7], and Board[8] == X (ACROSS BOTTOM)
#                       IV. if Board[0], Board[3], and Board[6] == X (DOWN LEFTMOST)
#                       V. if Board[1], Board[4], and Board[7] == X (DOWN MIDDLE)
#                       VI. if Board[2], Board[5], and Board[8] == X (DOWN RIGHTMOST)
#                       VII. if Board[0], Board[4], and Board[8] == X (DIAGONAL SLOPE DOWN)
#                       VIII. if Board[2], Board[4], and Board[6] == X (DIAGONAL SLOPE UP)
#               B. This checker method should be called on after each move? Sure
#               C. THE CHECKER MUST END THE GAME IF ONE OF THE CONDITIONS IS MET
#                 
# 0 1 2
# 3 4 5 
# 6 7 8 
