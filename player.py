# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math
import random

# creating a base plater classs
class Player:
    # self is a parameter used to access the current instance of the class, passing itself.
    def __init__(self, letter):
        # letter is either x or o
        self.letter = letter

    # we want all player to be able to get their next move
    def get_move(self,game):
        # we are passing here as ontop of this we are going to build a random computer player and human player
        pass

# here we are going to use inheritance to build a random computer player and human computer player that build atop the base computer player object
class RandomComputerPlayer(Player):
    def __init__(self,letter):
        # we need to initialise the super class (Player)
        super().__init__(letter)

    def get_move(self,game):
        
        # get a random valid spot for the computers move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        # we need to initialise the super class (Player)
        super().__init__(letter)

    def get_move(self,game):
        
        # defining values to initiate the HumanPlayers Turn
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')

            # when the user passes an input we need to ensure its valid
            # -- wrap it in a tranche
            try:
                
                # first check ensures that what the user enters (square) is an int 
                val = int(square)
                
                # second check ensures its an int thats availble in game
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            # defining how to handle the error.
            except ValueError:
                print('Invalid square. Try again.')

        return val
        
            


# %%



