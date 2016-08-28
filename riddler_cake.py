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
print computecylindervolume(1.0,1.0)
print computecakelayervolume(0,5.0,10.0,2.0)
print computetotalcakevolume(1.0,2.0,3.0,5.0,1.0)
print findoptimalcake(1000,1000,5)