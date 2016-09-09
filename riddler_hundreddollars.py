''' 
from http://fivethirtyeight.com/features/



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
        if current == -1:  current = 3
        if current == 4: current = 0
        
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

(46, 100, 0.46)
(487, 1000, 0.487)
(4677, 10000, 0.4677)
(46594, 100000, 0.46594)

Which equals 7/15 = 0.467

"""