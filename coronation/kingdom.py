""" The Puzzle of the Lonesome King
from  http://fivethirtyeight.com/features/the-puzzle-of-the-lonesome-king/

The childless King of Solitaria lives alone in his castle. Overly lonely, 
the king one day offers one lucky subject the chance to be prince or princess 
for a day. The loyal subjects leap at the opportunity, having heard tales of 
the opulent castle and decadent meals that will be lavished upon them. The 
subjects assemble on the village green, hoping to be chosen.

The winner is chosen through the following game. In the first round, every 
subject simultaneously chooses a random other subject on the green. 
(It is possible, of course, that some subjects will be chosen by more than one 
other subject.) Everybody chosen is eliminated. (Not killed or anything, just 
sent back to their hovels.) In each successive round, the subjects who are 
still in contention simultaneously choose a random remaining subject, and 
again everybody chosen is eliminated. If there is eventually exactly one 
subject remaining at the end of a round, he or she wins and heads straight to 
the castle for feting. However, it is also possible that everybody could be 
eliminated in the last round, in which case nobody wins and the king remains 
alone. If the kingdom has a population of 56,000 (not including the king), is 
it more likely that a prince or princess will be crowned or that nobody will 
win? """

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
    """ The King selection game, from the 538 riddler
    from http://fivethirtyeight.com/features/the-puzzle-of-the-lonesome-king/"""
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
        """ Executes one round of the king selection game.
        Requires the kingdom to be populated prior to the round."""
        
        # let every subject eliminate a subject
        for i in range(0, self.numbersubjectsatroundstart):
            self.eliminatesubject(self.subjects[i]
                      .choosewhomtoeliminate(self.numbersubjectsatroundstart))
                      
        # delete all the subjects who have been eliminated              
        for i in range(self.numbersubjectsatroundstart-1, -1, -1):  
            if self.subjects[i].iseliminated(): 
                del self.subjects[i]
                # print("deleted subject",i)  
            
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
            #print("end of round",i)
            #print(self.numbersubjectsatroundstart,"left")
            i += 1
        if self.numbersubjectsatroundstart == 1: 
            print("Win")
            return True
        print("False")    
        return False
        
""" Let's run some simulations

67 Wins,  100 Games,  67.0 Percent Wins
65 Wins,  100 Games,  65.0 Percent Wins
58 Wins,  100 Games,  58.0 Percent Wins
671 Wins,  1000 Games,  67.1 Percent Wins

So, it looks like the game results in a winner approximately 2/3 of the time.


""""        