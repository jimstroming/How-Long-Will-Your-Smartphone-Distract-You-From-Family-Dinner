import sys
from kingdom import Kingdom

class Menu:
    """ Take input and call the simulation """
    def __init__(self):
        self.kingdom = Kingdom()

    def run(self):
        """ Get the number of simulations and number of subjects 
        If either is zero, we exit the simulation """
        
        subjects = int(input("Enter number of subjects: "))
        loopcount = int(input("Enter number of games to play: "))
        
        successes = 0
        
        for i in range(0,loopcount):
            if self.kingdom.playgame(subjects):
                successes += 1
                
        print(successes,"Wins, ", loopcount, "Games, ", successes*100/loopcount, "Percent Wins" )        

if __name__ == "__main__":
    Menu().run()
    
    