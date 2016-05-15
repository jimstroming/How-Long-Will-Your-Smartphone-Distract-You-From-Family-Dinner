# The riddler martini glass problem
# from http://fivethirtyeight.com/features/can-you-solve-the-puzzle-of-the-overflowing-martini-glass/
# Its Friday. Youve kicked your feet up and have drunk enough of your martini that, 
# when the conical glass is upright, the drink reaches some fraction p of the 
# way up its side. 
# When tipped down on one side, just to the point of overflowing, how far does the 
# drink reach up the opposite side?

# Lets approach this computationally.
# Start with a cone of a given size
# Choose a pour point on the rim of the glass.  We will always use this pour point.
# Choose a point on the opposite side.  
# Construct a plane between the point point and the opposite point.
# Calculate how much wine is in the glass at that pouring angle.
# Calculate what the corresponding point would be is the glass was upright.

# do this for a number of number of opposite side points.  
# See if we can discern a pattern.

# Let's put the origin at the tip of the code.
# z in the direction of the height of the cone.
# x,y the other two directions.

# So for a cone of height H, and radius R,
# a point is inside the glass if

# (x^2+y^2) < (Rz/H)^2

# The pour point will be (x,y,z) = (R,0,H)
# The opposite side point will be  (Rs/H,0,s)

# m = slope in the x-z plane = delta z/ delta x = (H-s)/(R-Rs/H)

# Liquid in the glass will be points in the cone
# that also satisfy  
# (z-z1) < m(x-x1)
# (z-H)  < (H-s)(x-R)/(R-Rs/H)

# Let's start writing some functions.

import math

def calculatevolume(H,R,Z):
    # find the volume of liquid for a cone
    # of height H, radius R,
    # and filled up to Z, where Z=H is full
    # and Z = 0 is empty.
    # V of a cone = 1/3*(pi*r^2*h)

    radius = R*Z/H
    volume = (math.pi * radius**2 * Z)/3
    return volume
    
def calculatevolumeincrementally(H,R,Z):
    # find the volume of liquid for a cone
    # by checking each point in the cone
    # Compare the accuracy to the above method.
    # We will need to use this method for the tilted
    # glass, and want to make sure it is accurate.

    # find the volume of liquid for a cone
    # of height H, radius R,
    # and filled up to Z, where Z=H is full
    # and Z = 0 is empty.

    volume = 0;
    for z in range (0,int(0.5+Z)):
        radius = int(0.5+z*R/H)
        for y in range(-radius, radius):
            for x in range(-radius, radius):
                if (x**2 + y**2 < radius**2):
                    volume += 1;

    return volume;

def calculatefillheight(H,R,V):
    # calculate the fill height
    # given the Volume V, Height H, and Radius R

    denominator = math.pi * R**2 / (3 * H**2)
    fraction = V / denominator
    return fraction ** 0.3333


R = 1000
H = 2000

volume = calculatevolume(H,R,0.2*H)
print volume
print calculatevolumeincrementally(H,R,0.2*H)

print calculatefillheight(H,R,volume)