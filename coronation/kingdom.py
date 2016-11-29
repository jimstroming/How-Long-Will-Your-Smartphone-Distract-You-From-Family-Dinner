import random

class Subject:
    """ A citizen in the kingdom.  Each round, he will be called 
    to choose which fellow citizen to eliminate from the game"""
    def choosewhomtoeliminate(self, numbersubjects):
        """Choose which fellow citizen to eliminate from the game.
        Will be between 0 and numbersubjects-1 inclusive"""    
        return random.randint(0,numbersubjects-1)
        
class Kingdom:

    def __init__(self):
        """ Initialize a kingdom with no subjects. """
        self.subjects = []
        self.numbersubjectsatroundstart = 0
        
    def populatekingdom(self, numbersubjects):
        """ 