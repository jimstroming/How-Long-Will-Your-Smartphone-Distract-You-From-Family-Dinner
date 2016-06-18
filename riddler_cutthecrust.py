"""
from http://fivethirtyeight.com/features/can-you-solve-the-puzzle-of-the-picky-eater/


Every morning, before heading to work, you make a sandwich for lunch using perfectly 
square bread. But you hate the crust. You hate the crust so much that youll only eat 
the portion of the sandwich that is closer to its center than to its edges so that 
you dont run the risk of accidentally biting down on that charred, stiff perimeter. 
How much of the sandwich will you eat?

"""

"""

Let's try solving pythonically.


"""

import pdb


def calculateclosetocrust(sidelength):
    center = float(sidelength)/2
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
    print centercount
    print crustcount
    return float(centercount) / (centercount + crustcount)
    
print calculateclosetocrust(100)    
print calculateclosetocrust(1000)                    
print calculateclosetocrust(10000)                    
