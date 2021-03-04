# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from player import HumanPlayer, RandomComputerPlayer
import math
import time

class TicTacToe:
    def __init__(self):
        
        # using a list to create the 3x3 ttt board, we can later assign an index to each space
        self.board = [' ' for _ in range(9)]
        
        # keeps track of current winner
        self.current_winner = None 

    # creating the board
    def print_board(self):
            
        # getting our rows, this is indexinig into our len 9 list
        # defining which group of 3 spaces are we choosing passing 0,1,2 as i [i*3:(i+1)*3].
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
                
            # for each row, print seperators and join then in a string where the seperatpor is |
            print('| ' + ' | '.join(row) + ' |')

    # static method because it doesnt relate to any specidfic board we dont need to pass in a self
    @staticmethod
    def print_board_nums():

        # tells us what numbers corresponds to what box
        # gives you what indicies there are for each row
        number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]

        #concatenate this now for  
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # ITS GAME TIME
    # given this board we are representing the emtpy spaces with a space

    # We need to know the available moves after a move is made
    def available_moves(self):
            
        # -- SIMPLER WAY -- list comprehension
        return [i for i, spot in enumerate(self.board) if spot == ' ']

        # -- THIS TRANSLATES TO THE ABOVE --

        # empty list to begin with
        #- moves = []

        # enumerate will essentially create a list and assign tuples that have the (index, value) at that index i.e.
        #- for (i,spot) in enumerate(self.board)

            # ['x', 'x', 'o', ' ' ] ---> [ (0,'x') , (1,'x'), (2,'o'), (3,' ') ]
            # if spot = space we know its empty and its an available move
            #- if spot == ' ':

                #append the index 
                #- moves.append(i)
                
            #-return moves
            
        # -- END OF TRANSLATION --
        
    # checks if there are empty spaces on the board
    def empty_squares(self):

        #this will return a boolean
        return ' ' in self.board

    # checks how many empty spaces there are on the board
    def num_empty_squares(self):
        return self.board.count('')

    # Definiging the make a move functionality
    # to make a move we need to know the move itself 'Self' the location 'square' and whether is X or O 'letter'
    def make_move(self, square, letter):
            
        #
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # checking for the winner
    def winner (self, square, letter):
            
        # Checking which row by diving by 3 and rounding down i.e. 5 is in row index 1 which is the second row
        row_ind = square // 3
            
        # Given the row index get the entire row, i.e. row index of 1 means [3:6] upto not including
        row = self.board[row_ind*3:(row_ind + 1)* 3]
            
        # checking for 3 of the same letter in the row
        if all([spot == letter for spot in row]):
            return True
            
        # if rows dont match check column, here we divide by 3 and take the left over i.e. 8/3 leaves you with column ind 2 the last column
        col_ind = square % 3

        # using maths you can return values 2,5,8 using the formula below
        column = [self.board[col_ind+i*3] for i in range(3)]

        # checking for 3 of the same letter in the col
        if all([spot == letter for spot in column]):
            return True

        # if columns dont match checking the diaganals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [ 0 , 4 , 8 ] ]
                
            # checking for 3 of the same letter in the diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
                
            diagonal2 = [self.board[i] for i in [ 2 , 4 , 6 ] ]

            # checking for 3 of the same letter in the diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
                
        # IF ALL THESE FAIL WE DO NOT HAVE A WINNER

        return False  

def play(game, x_player, o_player, print_game=True):
    
    if print_game:
        game.print_board_nums()

    # Starting letter
    letter = 'X' 

    # while the game still has empty squares repeat the game
    while game.empty_squares():

        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #empty line for spacing.

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # After we made our move, we need to alternate letters
        
            # ---SIMPLER WAY TO WRITE IT---
            #- letter = 'O' if letter =='X' else 'X'

            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
        
        # tiny break
        time.sleep(1)

    if print_game:
        print('it\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player =  RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

            




# %%



