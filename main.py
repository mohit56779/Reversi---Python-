import reversi
def main():
    while True :
        game = reversi.Reversi()
        print('Starting new game!')
        print('Black goes first, then white')
        
        while True:
            playerColour = input("Enter 'b' to choose to play black, 'w' to choose white:")
            if playerColour == 'b' or playerColour == 'w':
                break
        
        
        
        game.setPlayerColour(playerColour)
        
        while True:
            mode = input("Enter '1' to choose easy computer opponent, '2' for hard computer opponent:")
            if mode == "1" or mode == "2":
                break
            
        # displaying board and score
        game.displayBoard()
        
        displayScore(game)
        # finding if it's player's turn or not
        if playerColour == 'w':
            playerTurn= False
            
        else:
            playerTurn = True
            
        
        while True:
            
            # runs only if it's computer's turn
            if playerTurn == False:
                
                # if mode is '2' we use makeMoveSmart() method, if not then makeMoveNaive()
                if mode == '2':
                    
                    # if there's no moves left for the current player we break out
                    if game.isGameOver == True:
                        print("Game over!")
                        break
                    game.makeMoveSmart()
    
                else:
                    if game.isGameOver == True:
                        print("Game over!")
                        break                
                    game.makeMoveNaive()
                    
                # display board and score and change turn
                game.displayBoard()
                displayScore(game)
                playerTurn = True
                
            # runs when it's player's turn   
            if playerTurn == True:
                print("Enter 2 numbers from 0-7 separated by a space to make a move,")
                print("   where the first number is the row and the second number is the column")
                print("Enter 'q' to quit.")
                
                # forever loop until we get a right input
                while True:
                    inputMove = input("Enter move:")
                    
                    # checking if player wants to quit
                    if inputMove == 'q':
                        print("Game over!")
                        game.displayBoard()
                        displayScore(game)
                        break 
                    
                    splittedMove = inputMove.split(" ")
                    
                    # we try to put the input as ints, if there's an exception (if user gave wrong inputs) we print and stay in while loop
                    try:
                        moveTuple = (int(splittedMove[0]),int(splittedMove[1]))
                        break
                    except:
                        print("Wrong input. Try Again!")
                        
                # if player wants to quit break out of outer loop as well
                if inputMove == 'q':
                    break
                # if the position is valid then only make move    
                if game.isPositionValid(moveTuple,playerColour):
                    if game.isGameOver == True:
                        print('Game over!')
                        break  
                    game.makeMovePlayer(moveTuple)
                    game.displayBoard()
                    displayScore(game)
                    playerTurn = False
                else:
                    
                    # checking the kind of error
                    if moveTuple[0] > game.SIZE or moveTuple[1] > game.SIZE:
                        print("Invalid position: out of bound.")
                    else:
                        print("Invalid position: piece doesn't surround line of opponent pieces.")
            
        playAgain = input("Do you want to play again (y/n)?")
            
        if playAgain == "n":
            print("Goodbye!")
            break
            
            
"""
        Functionality:
            prints score of both playersz
        Parameters:
            game: Reversi game object
            playerColour: what colour the player is player with either 'w' or 'b'
"""            
        
    
def displayScore(game):
    print('Score: white %i, black %i'%(game.getScore('w'),game.getScore('b'))) 
    
main()