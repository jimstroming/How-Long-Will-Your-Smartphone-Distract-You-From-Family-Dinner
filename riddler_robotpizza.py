''' 
from fivethirtyeight.com


'''

import random
import math
import pdb



def randompoint():

    pointdegrees = random.randint(0, 360)
    pointradians = math.radians(float(pointdegrees))
    x = math.cos(pointradians)
    y = math.sin(pointradians)
    
    return x,y


def checkifintersect(ex1,ey1,fx2,fy2,gx1,gy1,hx2,hy2):
    # put line  EF in slope intercept form.
    # y = mx + b
    
    # find the line with slope m that G lies on
    # y = mx + c
    
    # find the line with slope m that H lies on
    # y = mx + d
    
    # if b between c and d, then the lines intersect
     


    return False



def timetoeat():

    yourtime = random.randint(1,5)    # the current time when you are done with a task 
    sistertime = random.randint(1,5)  # the current time when your sister is done with a task

    while (yourtime != sistertime):
        if yourtime < sistertime:
            yourtime += random.randint(1,5)
        else:
            sistertime += random.randint(1,5)

    return yourtime

def averagetimetoeat(iterations):
    totaltime = 0
    for x in range (0,iterations):
        totaltime += timetoeat()
    return float(totaltime)/iterations

pdb.set_trace()
