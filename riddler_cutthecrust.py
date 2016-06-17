"""
from 

"""

"""

Let's try solving pythonically


"""

import pdb


def calculateclosetocrust(sidelength):
    center = sidelength/2
    centercount = 0
    crustcount  = 0
    for x in range (0,sidelength):
        leftdist  = x
        rightdist = sidelength - x
        xdist = min(leftdist, rightdist)
        for y in range(0, sidelength):
            bottomdist = y
            topdist = sidelength - y
            crustdist = min(bottomdist, topdist, xdist)
            crustdistsquared = crustdist^2
            centerdistsquared = (center-x)*(center-y)
            if centerdistsquared < crustdistsquared:
                centercount += 1
            else:
                crustcount += 1
    return float(centercount) / (centercount + crustcount)
    
print calculateclosetocrust(100)    
print calculateclosetocrust(1000)                    
print calculateclosetocrust(3000)                    
