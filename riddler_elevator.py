'''
from fivethirtyeight.com
http://fivethirtyeight.com/features/can-you-solve-this-elevator-button-puzzle/
In a buildings lobby, some number (N) of people get on an elevator that goes to 
some number (M) of floors. There may be more people than floors, or more floors than people. 
Each person is equally likely to choose any floor, independently of one another. 
When a floor button is pushed, it will light up.
What is the expected number of lit buttons when the elevator begins its ascent?
'''

# Let's start by working some examples by hand and see if we 
# can find a pattern.
# Let N by the number of people, M be the number of floors

# If N=1, then the expected value will always be 1.  One person
# can only press one button.
# If M=1, then the expected value will always be 1.  If there
# is only one floor, then only that button can be pressed.
# If M, the number of floors gets very large, then the expected 
# value will approach N.  On a million floor elevator, it is 
# very unlikely that two people will press the same floor.
# If N, the number of people gets very large, then the expected
# value will approach M.  If a million people are in the elevator,
# it is very likely they will press all the buttons.

# working out the cases when two people are in the elevator, N = 2
# N M  Expected value
# 2 1  1
# 2 2  3/2
# 2 3  5/3
# 2 4  7/4
# 2 5  9/5

# It looks like
# E(2,M) = 2M-1/M

# What about when 3 people are in the elevator?
# N M  E(N,M)
# 3 1  1  
# 3 2  7/4
# 3 3  19/9
# 3 4  37/16

# This is E(3,M) = (3M^2 - 3M + 1)/(M^2)

# The sequences in the numerator are familiar.
# 1, 3, 5, 7, 9
# 1, 7, 19, 37
# These are Nexus numbers.
# Nexus numbers have the format
# Nexus(d,n) = (n+1)^(d+1) - n^(d+1)

# In our case, 
# d = N-1, n = M-1
# E(N,M) = Nexus(N-1, M-1)/M^(N-1)
#        = (M^N - (M-1)^N)/(M^(N-1))

# Let's verify this is true by running a simulation for 
# values on N and M and comparing it to the above equation.

import sys
import random

def simulateelevator(people, floors):

    buttonspressed = []
    for x in range (0, people):
        button = random.randint(1,floors)
        if not button in buttonspressed:
            buttonspressed.append(button)
    return len(buttonspressed)

def runmultiple(people, floors, times):
    total = 0.0;
    for x in range (0, times):
        total += simulateelevator(people, floors)
    return float(total)/times

def elevatorequation(N, M):
    people = float(N)
    floors = float(M)
    numerator   = pow(floors, people) - pow(floors-1.0, people)
    denominator = pow(floors, people-1.0)
    return float(numerator)/denominator

print "Running simulation"
print "Will print any differences > 1%"
for x in range (1, 100):
    for y in range (1, 100):
        simulated = runmultiple(x,y,1000)
        calculated = elevatorequation(x,y)
        if abs(simulated-calculated > 0.01*simulated):
         print x, y, simulated, calculated
    

 
