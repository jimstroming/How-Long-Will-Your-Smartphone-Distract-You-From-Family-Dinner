import random

class Subject:
    """ A citizen in the kingdom.  Each round, he will be called 
    to choose which fellow citizen to eliminate from the game"""
    def __init__(self):
        """ Initialize the Subject as not eliminated from the game"""
        self.eliminated = False
        
    def iseliminated(self):
        """ Returns True if the subject is eliminated """
        return self.eliminated
        
    def eliminate(self):
        """ Eliminated the Subject from the game """
        self.eliminated = True
    
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
        """ fill the kingdom with numbersubjects subjects """
        self.subjects = []
        for i in range(0,numbersubjects):
            self.subjects.append(Subject())
            
    def eliminatesubject(self, subjectnumber):
        """ eliminate the subject  """
        self.subjects[subjectnumber].eliminate()