
"""
    - self.gameBoard represents the game board
    - self.playerColour represents the colour of the human player
    - self.computerColour represents the colour of the computer
    - the colour arguments are eiter self.WHITE or self.BLACK, which are defined below
    - self.colourPlaying is the colour who has to make the move currently
"""


class Reversi:
    WHITE = "w"
    BLACK = "b"
    EMPTY = "."
    SIZE = 8
    

    def __init__(self):
        self.gameBoard = []
        self.playerColour = 'b'
        self.computerColour = 'w'
        self.colourPlaying = 'b'
        self.newGame()


    """
    Functionality:
        Create the game state so players can play again
    Parameters: 
        None
    """
    def newGame(self):
        
        # making the board by adding 8 lists of 8 objects
        for i in range(0, 8):
            self.gameBoard.append([])
            
            for j in range(0,8):
                self.gameBoard[i] = self.gameBoard[i] + [Reversi.EMPTY]
        
        # initial starting pieces        
        self.gameBoard[3][4] = Reversi.BLACK
        self.gameBoard[3][3] = Reversi.WHITE
        self.gameBoard[4][3] = Reversi.BLACK
        self.gameBoard[4][4] = Reversi.WHITE
      
        




    """
    Functionality:
        Return the score of the player
    Parameters:
        colour: The colour of the player to get the score for 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def getScore(self, colour):
        
        # iterating through the entire board and checking colour to get the score
        score = 0
        for row in self.gameBoard:
            for element in row:
                if element == colour:
                    score+=1
                
                
        return score


    """
    Functionality:
        Set the colour for the human player to the designated colour, as well as the computer will haev the other colour
    Parameters:
        colour: The colour of the player the user wants to play as 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def setPlayerColour(self, colour):
        
        # setting player and computer Colours according  to the parameter
        if colour == 'b':
            self.playerColour = 'b'
            self.computerColour = 'w'
        else:
            self.playerColour = 'w'
            self.computerColour = 'b'
            


    """
    Functionality:
        Print out the current board state
        The index of the rows and columns should be on the left and top.
        See the sample output for details
    Parameters: 
        None
    """
    def displayBoard(self):
        
        # priting the board with the indexes for row and column with format
        print("  0 1 2 3 4 5 6 7")
        for row in range(len(self.gameBoard)):
            print(str(row), end =' ')
            for element in self.gameBoard[row]:                
                print(element,end=' ')
            
            print("")


    """
    Functionality:
        Return true if the input position 'position' is valid for the given player 'colour' to make
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def isPositionValid(self, position, colour):
        # if the position is out of bound
        if position[0] >= Reversi.SIZE or position[1] >= Reversi.SIZE:
            return False
        
        # if the position is not empty
        if(self.gameBoard[position[0]][position[1]]) != Reversi.EMPTY:
            return False
        
        # get all the flip_lists in all 8 directions for the position    
        list_1 = self.flip_list(position, colour,(-1,-1))
        list_2 = self.flip_list(position, colour,(+1,+1))
        list_3 = self.flip_list(position, colour,(+1,-1))
        list_4 = self.flip_list(position, colour,(-1,+1))
        list_5 = self.flip_list(position, colour,(-1,0))
        list_6 = self.flip_list(position, colour,(+1,0))
        list_7 = self.flip_list(position, colour,(0,-1))
        list_8 = self.flip_list(position, colour,(0,+1))   
        
        # if the list is not empty then there is a valid flipable move
        if list_1 != [] or list_2 != [] or list_3 != [] or list_4 != [] or list_5 != [] or list_6 != [] or list_7 != [] or list_8 != []:
            
            return True
        
        return False
    
    """
    Functionality:
    Returns a list of positions that should be flipped if a move is made in a position, returns an empty list if the move is invalid 
        
    Parameters: position - a tuple in (row,column) format 
                colour - colour of the player making the move, either 'b' or 'w'
                direction - a tuple which tells the direction we need to check, there are 8 directions for a position.In the direction tuple the numbers indicate the movement along rows and colums required to get that direction from the piece, first element for row and second for column. Directions are as follows -
                        (-1,+1) - diagonal direction which starts from upper right of the board downwards
                        (+1,-1) - doagonal direction which starts from upper right of the board upwards
                        (-1,-1) - diagonal direction which starts from upper reft of the board upwards
                        (+1,+1) - diagonal direction which starts from upper reft of the board downwards
                        (0, +1) - direction along the same row downwards
                        (0, -1) - direction along the same row upwards
                        (+1, 0) - direction along the same column rightwards
                        (-1, 0) - direction along the same column leftwards
                        
                
    """
    def flip_list(self, position, colour,direction):
        # breaking down direction into row and column movements
        row_movement = direction[0]
        column_movement = direction[1]
        
        # checking which colour is playing and which colour is opposition
        if colour == 'b':
            move_maker = 'b'
            oppos = 'w'
        else:
            move_maker = 'w'
            oppos = 'b'  
            
        # variables to start the first occurence we ecounter for opposition piece and player piece
        first_index_oppos = (-1,-1)
        first_index_player = (-1,-1)
        
        # a list to store the opposition pieces which can be flipped according to the rules
        flipable_pieces= []
        
        # if the first occurences are found
        player_piece_found = False
        opposition_piece_found= False
        
        # getting row and column of position
        column = position[0]
        row = position[1]
        
        # looping to get the first occurences
        for index in range(len(self.gameBoard)):  
            column = column + column_movement
            row = row + row_movement
            
            # if out of bound
            if column >=0 and row >=0 and column< len(self.gameBoard) and row< len(self.gameBoard):
                
                #if we found the first occurence of player piece  
                if self.gameBoard[column][row] == move_maker:
                    if player_piece_found == False:
                        first_index_player = (row,column)
                        
                        player_piece_found = True
                        
                # for all occurences of opposition pieces
                elif self.gameBoard[column][row] == oppos:
                    
                    # if the player's piece is found stop adding to the flipable_pieces, since we don't flip after the player piece
                    if player_piece_found == False:
                        flipable_pieces.append((column,row))
                        
                    # storing the first occurence
                    if opposition_piece_found == False:
                        first_index_oppos = (row,column)
                        opposition_piece_found = True
                        
                #i if there is an empty or '.' in between
                else:
                    break
        
        # if both first occurences found
        if player_piece_found == True and opposition_piece_found == True:
            
            # different direcrions will require different checks
            if direction == (-1,+1) or direction == (-1,-1) or  direction == (-1,0):
                if first_index_player[0] < first_index_oppos[0]:
                    return flipable_pieces
            elif direction == (+1,-1) or direction == (+1,+1) or  direction == (+1,0):
                if first_index_player[0] > first_index_oppos[0]:
                    return flipable_pieces
            elif direction == (0,+1):
                if first_index_player[1] > first_index_oppos[1]:
                    return flipable_pieces
            elif direction == (0,-1):
                if first_index_player[1] < first_index_oppos[1]:
                    return flipable_pieces
                    
        # return empty list if the position is invalid in the given direction      
        return []        


    """
    Functionality:
        Return true if the game is over, false otherwise
        The game is over when the current player cannot make any more legal moves.
    Parameters: 
        None
    Note: 
        Skipping is not allowed
    """
    def isGameOver(self):
        
        # if the colourPlaying has no valid moves left
        if len(self.allValidMoves(self.colourPlaying)) == 0:
            return True
        
        return False
    '''
    Functionality:
        returns a list of all valid positions for a colour at the present game
    Paramaters
        colour -> string 'w' or 'b' representing black or white colour   
    '''
    def allValidMoves(self,colour):
        valid_moves = []
        
        # iterating over the whole board and finding all valid moves
        for row in range(len(self.gameBoard)):
            for column in range(len(self.gameBoard)):
                if self.isPositionValid((row,column),colour) == True:
                    valid_moves.append((row,column))
        return valid_moves
                
        
    """
    Functionality: 
        Make the given move for the human player, and capture any pieces
        If you assume the move is valid, make sure the validity is checked before calling
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
    """
    def makeMovePlayer(self, position):
        self.makeMove(position,self.playerColour)
            
        
    '''
    Functionality:
                 given a position and colour playinh this method will make a move i.e flip the position pieces of all the opposition pieces according to the rules of the game.
    Parameters:
                position: position of move
                colour : the colour playing either 'w' or 'b'
    '''
    def makeMove(self,position,colour):
        directions = [(-1,+1), (+1,-1) ,(1,-1),(+1,+1),(0, +1) ,(0, -1),(+1, 0) ,(-1,0)]
        flip_list = []
        for item in directions:
            flip_list_in_this_dir = self.flip_list(position,colour,item)
            flip_list = flip_list + flip_list_in_this_dir
       # print(flip_list)
       
        self.gameBoard[position[0]][position[1]] = colour
        for item in flip_list:
           
            self.gameBoard[item[0]][item[1]] = colour        
        

    """
    Functionality:
        Make a naive move for the computer
        This is the first valid move when scanning the board left to right, starting at the top
    Parameters: 
        None
    """
    def makeMoveNaive(self):
        
        # get all valid moves possible for computer currently and use position[0]
        position = self.allValidMoves(self.computerColour)[0]
        self.makeMove(position,self.computerColour)
        print('Computer making move:' + str(position))
        
        


    """
    Functionality:
        Make a move for the computer which is the best move available
        This should be the move that results in the best score for the computer
    Parameters: 
        None
    """
    def makeMoveSmart(self):
        
        # getting all valid moves that computer can make
        position_list = self.allValidMoves(self.computerColour)
        
        #all the 8 directions
        directions = [(-1,+1), (+1,-1) ,(1,-1),(+1,+1),(0, +1) ,(0, -1),(+1, 0) ,(-1,0)]
        
        # creating empty list and tuple variable to store the biggest flip list we will find and the position which got it
        biggest_flip_list = []
        position_selected = (100,100)
        
        # iterating through all the positions
        for position in position_list:
            
            # finding all the opposition pieces that will be flipped for each position
            flip_list=[]
            for direction in directions:
                flip_list_in_this_dir = self.flip_list(position,self.computerColour,direction)
                flip_list = flip_list + flip_list_in_this_dir
            
            # finding the biggest flip_list
            if len(flip_list) > len(biggest_flip_list):
                biggest_flip_list = flip_list
                position_selected = position
                
        # fliping the pieces
        self.gameBoard[position_selected[0]][position_selected[1]] = self.computerColour
        for item in biggest_flip_list:   
            self.gameBoard[item[0]][item[1]] = self.computerColour
        
        # printing the move computer made   
        print('Computer making move:' + str(position_selected))

        
            
            


            
    
    


