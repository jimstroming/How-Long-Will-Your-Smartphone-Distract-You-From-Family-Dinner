''' 
from http://http://fivethirtyeight.com/features/who-keeps-the-money-you-found-on-the-floor/

You and four statistician colleagues find a $100 bill on the floor of your department’s faculty lounge. 
None of you have change, so you agree to play a game of chance to divide the money 
probabilistically. The five of you sit around a table. The game is played in turns. 
Each turn, one of three things can happen, each with an equal probability: The bill 
can move one position to the left, one position to the right, or the game ends and the person 
with the bill in front of him or her wins the game. You have tenure and seniority, 
so the bill starts in front of you. 
What are the chances you win the money?



'''

import random
import math
import pdb

# Now let's try the pythonic solution

def runonesimulation():

    current = 0
    
    while (True):
        increment = random.choice([-1,0,1])
        if increment == 0: return current
        current += increment
        if current == -1:  current = 4
        if current == 5: current = 0
        
def runmanygames(count):
    zerowinners = 0
    for x in range (0,count):
        winner = runonesimulation()
        #print winner
        if winner == 0:  zerowinners += 1
        
    return zerowinners, count, float(zerowinners)/count        
    
        
print runmanygames(100)
print runmanygames(1000)
print runmanygames(10000)
print runmanygames(100000)
print makemanypizzas(1000000)

""" 
Which gives





"""