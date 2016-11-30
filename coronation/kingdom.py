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
        
    def populate(self, numbersubjects):
        """ Fill the kingdom with numbersubjects subjects """
        self.subjects = []
        for i in range(0,numbersubjects):
            self.subjects.append(Subject())
        self.numbersubjectsatroundstart = numbersubjects    
            
    def eliminatesubject(self, subjectnumber):
        """ Eliminate the subject  """
        self.subjects[subjectnumber].eliminate()
        
    def playaround(self):
        """ Executes one round of the king selection game
        Requires the kingdom to be populated prior to the round."""
        
        # let every subject eliminate a subject
        for i in range(0, self.numbersubjectsatroundstart):
            self.eliminatesubject(self.subjects[i]
                      .choosewhomtoeliminate(self.numbersubjectsatroundstart))
                      
        # delete all the subjects who have been eliminated              
        for i in range(self.numbersubjectsatroundstart-1, -1, -1):  
            if self.subjects[i].iseliminated(): 
                del self.subjects[i]
                print("deleted subject",i)  
            
        # count the numberofsubjects
        self.numbersubjectsatroundstart =  len(self.subjects)   
        
    def playgame(self, subjectnumber):
        """ Executes the king selection game.
        Returns True if one subject remains at the end.
        Returns False if no subjects remain at the end. """
        
        self.populate(subjectnumber)
        i = 1;
        while (self.numbersubjectsatroundstart > 1):
            self.playaround()
            print("end of round",i)
            print(self.numbersubjectsatroundstart,"left")
            i += 1
        if self.numbersubjectsatroundstart == 1: return True
        return False