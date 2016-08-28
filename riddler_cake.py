"""Can you bake the optima cake.
From the 538 riddler
http://fivethirtyeight.com/features/can-you-bake-the-optimal-cake/

A mathematician who has a birthday coming up asks his students to 
make him a cake. He is very particular (he is a constructive set 
theorist, which explains a lot) and asks his students to make him a 
three-layer cake that fits under a hollow glass cone he has on his desk. 
(The cone was given to him as a prize for proving an obscure theorem 
long ago.) He requires that the cake fill up the maximum amount of 
volume under the cone as possible and that the layers of the cake 
have straight vertical sides. (Again, the guys particular.) What are 
the thicknesses of the three layers of the cake in terms of the height 
of the glass cone? What percentage of the cones volume does the cake 
fill?

"""


# Let's start writing some functions.

import math

def computecylindervolume(height, radius):
    return math.pi*radius*radius*height
    

def computecakelayervolume(layerbottom, layertop, coneheight, conebaseradius):
    # radius of the layer is based on the top of the layer
    radius = conebaseradius * (coneheight-layertop)/coneheight
    return computecylindervolume(layertop-layerbottom,radius)

def computetotalcakevolume(top1,top2,top3, coneheight, conebaseradius):
    totalvolume = 0
    totalvolume += computecakelayervolume(0,    top1, coneheight, conebaseradius)
    totalvolume += computecakelayervolume(top1, top2, coneheight, conebaseradius)
    totalvolume += computecakelayervolume(top2, top3, coneheight, conebaseradius)
    return totalvolume

def findoptimalcake(coneheight, conebaseradius, stepsize):
    maxvolume = 0
    maxtop1 = 0
    maxtop2 = 0
    maxtop3 = 0
    
    for top1 in range(0, coneheight, stepsize):
        for top2 in range(top1, coneheight, stepsize):
            for top3 in range(top2, coneheight, stepsize):
                newvolume = computetotalcakevolume(top1,top2,top3, coneheight, conebaseradius)
                if newvolume > maxvolume:
                    maxvolume = newvolume
                    maxtop1 = top1
                    maxtop2 = top2
                    maxtop3 = top3

    return maxtop1, maxtop2, maxtop3, maxvolume 


# Let's run it a few times to get some data

print "findoptimalcake(1000,1000,2)"
print findoptimalcake(1000,1000,2)
print "findoptimalcake(500,500,2)"
print findoptimalcake(500,500,2)
print "findoptimalcake(500,1000,2)"
print findoptimalcake(500,1000,2)
print "findoptimalcake(1000,500,2)"
print findoptimalcake(1000,500,5)

"""
findoptimalcake(1000,1000,5)
(165, 345, 565, 734806348.00312)
findoptimalcake(500,500,5)
(80, 170, 280, 91850744.41300479)
findoptimalcake(500,1000,5)
(80, 170, 280, 367402977.65201914)
findoptimalcake(1000,500,5)
(160, 340, 560, 183701488.82600957)
findoptimalcake(1000,1000,2)
(162, 344, 562, 734839482.3808373)
findoptimalcake(500,500,2)
(82, 172, 282, 91852528.83763202)
findoptimalcake(500,1000,2)
(82, 172, 282, 367410115.35052806)
findoptimalcake(1000,500,2)
(160, 340, 560, 183701488.82600957)
"""

"""
The heights are proportional to the height of the cone, and are 
independent of the radius of the cone.

thickness1 = (162/1000) =     .16
thickness2 = (344-162)/1000 = .18
thickness3 = (562-344)/1000 = .22

volume of optimal cake with base 1000, height 1000 = 735,000,000
volume of cone with base 1000, height 1000 = pi*r^2*h/3 = 1.05 million

% cake fills = 735/1050 = 70%

"""