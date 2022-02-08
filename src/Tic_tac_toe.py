import numpy as np

# Class to represent tic tac toe game:
class Tic_tac_toe():
    # Constructor:
    def __init__(self, side = 3):
        self.board = [[0 for i in np.arange(side)] for j in np.arange(side)] # Creating board
        #self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.side = side # Saving variable with board length
    

    # Function to show board:
    def show_board(self):
        for i in np.arange(0, self.side):
            for j in np.arange(0, self.side):
                print(self.board[i][j], end=" ")
            print("")
    

    # Function to test if someone won:
    def checking_winer(self):

        # Checking rows:
        for row in np.arange(self.side):
            symb = self.board[row][0]

            if(symb == 0):
                continue
            
            for symbol in np.arange(1, self.side):
                if(symb == self.board[row][symbol]):
                    if(symbol == self.side - 1):
                        return True
                    continue
                else:
                    break

        
        # Checking columns:
        for col in np.arange(self.side):
            symb = self.board[0][col]

            if(symb == 0):
                continue
            
            for symbol in np.arange(1, self.side):
                if(symb == self.board[symbol][col]):
                    if(symbol == self.side - 1):
                        return True
                    continue
                else:
                    break
        

        # Checking main diagonal:
        for id in np.arange(self.side):
            symb = self.board[0][0]

            if(symb == 0):
                break
            
            if(symb == self.board[id][id]):
                if(id == self.side - 1):
                    return True
                continue
            else:
                break


        # Checking other diagonal:
        for id in np.arange(self.side):
            symb = self.board[self.side - 1][0]

            if(symb == 0):
                break

            if(symb == self.board[self.side - id - 1][id]):
                if(id == self.side - 1):
                    return True
                continue
            else:
                break
        

        return False        


    # Checking draw:
    def checking_draw(self):
        for i in np.arange(self.side):
            for j in np.arange(self.side):
                if(self.board[i][j] == 0):
                    return False
        
        return True


    # Checking if it is a valid movement:
    def valid_movement(self, x, y):

        # Checking if "x" is in the correct range:
        if(x < 0 or x >= self.side):
            return False
        
        # CHecking if "y" is in the correct range:
        if(y < 0 or y >= self.side):
            return False
        
        # Checking if the position is empty:
        if(self.board[x][y] != 0):
            return False
        
        return True


    # Function to make some movement:
    def movement(self, player):
        moving = True

        while(moving):
            x, y = map(int, input().split())

            if(self.valid_movement(x, y)):
                self.board[x][y] = player
                moving = False
            else:
                print("Invalid movement, please try again.")


    # Function to run for each player turn:
    def player_turn(self, player):
        
        self.show_board()

        print("It is {player} time: ".format(player = player), end="")

        self.movement(player)

        if(self.checking_winer()):
            print("Player {player} won this game!".format(player = player))
            self.game_on = False
        elif(self.checking_draw()):
            print("The game tied!")
            self.game_on = False


    # Function to run the game:
    def run(self):
        self.game_on = True
        print("Starting tic-tac-toe game!")

        while(self.game_on):
            
            self.player_turn("x")
            
            if(not self.game_on):
                break
            
            self.player_turn("o")
