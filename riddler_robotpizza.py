''' 
from http://fivethirtyeight.com/features/what-if-robots-cut-your-pizza/

At RoboPizza, pies are cut by robots. When making each cut, a robot will 
randomly (and independently) pick two points on a pizzas circumference, and then cut 
along the chord connecting them. If you order a pizza and specify that you want the 
robot to make exactly three cuts, what is the expected number of pieces your pie 
will have?


'''

import random
import math
import pdb

# Let's start with the pythonic solution

def getrandompoint():
    # Need a function to choose a random point on the circle
    # and return the x and y coordinates
    pointdegrees = random.random()*360 
    pointradians = math.radians(pointdegrees)
    x = math.cos(pointradians)
    y = math.sin(pointradians)    
    return x,y

# Need a function to determine if two chord intersect

def checkifintersect(ex,ey,fx,fy,gx,gy,hx,hy):
    # returns True if chord EF intersects chord GH
    
    # put line  EF in slope intercept form.
    # y = mx + b
    m = (fy-ey)/(fx-ex)
    b = fy-m*fx
    
    # find the y intercept c of the line with slope m that G lies on
    # y = mx + c
    c = gy-m*gx
    
    # find the y intercept d of line with slope m that H lies on
    # y = mx + d
    d = hy-m*hx
    
    
    # if b between c and d, then the lines intersect
    if b < c and c < d: return True
    if d <c  and c < b: return True 
    return False

def makeapizza():
    a1x, a1y = getrandompoint()
    a2x, a2y = getrandompoint()

    b1x, b1y = getrandompoint()
    b2x, b2y = getrandompoint()

    c1x, c1y = getrandompoint()
    c2x, c2y = getrandompoint()

    numberofpieces = 4  # if the slices do not insect, there will be four slices
    
    if checkifintersect(a1x,a1y,a2x,a2y,b1x,b1y,b2x,b2y):
        numberofpieces += 1  # each intersection adds a slice
    if checkifintersect(a1x,a1y,a2x,a2y,c1x,c1y,c2x,c2y):
        numberofpieces += 1    
    if checkifintersect(c1x,c1y,c2x,c2y,b1x,b1y,b2x,b2y):
        numberofpieces += 1
    return numberofpieces    
    
def makemanypizzas(count):
    piecetotal = 0
    for x in range (0,count):
        piecetotal += makeapizza()
    return piecetotal, count, float(piecetotal)/count        
    
        
print makemanypizzas(100)
print makemanypizzas(1000)
print makemanypizzas(10000)
print makemanypizzas(100000)
print makemanypizzas(1000000)

""" 
Which gives

(499, 100, 4.99)
(5075, 1000, 5.075)
(50145, 10000, 5.0145)
(499846, 100000, 4.99846)
(4999367, 1000000, 4.999367)

Which looks like 5 pieces on average.

"""