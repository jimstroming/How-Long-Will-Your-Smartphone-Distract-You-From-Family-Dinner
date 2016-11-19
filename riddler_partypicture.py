"""
From http://fivethirtyeight.com/features/the-puzzle-of-the-lonesome-king/

Five couples attend a party. They have hugged each other and said their goodbyes
but before they leave, the 10 people arrange themselves in a straight line at
random to take a photograph. (All possible lineups are equally likely.) What is 
the probability that no person in the line is standing next to his or her 
partner?
"""


"""
Let's start with the simpler cases and see if there is a pattern

2 couple party

1 2 3 4   together
1 2 4 3   together
1 3 2 4
1 3 4 2   together
1 4 2 3
1 4 3 2   together

So, for the 2 person party
P(together) = 4/6 = 2/3
P(not together) = 1/3

"""

"""
Let's do the 3 couple case.

1 2 x x x x  together   all 24/24 cases

1 3 2 4 5 6 together
1 3 2 4 6 5 together
1 3 2 5 4 6
1 3 2 5 6 4 together
1 3 2 6 4 5  
1 3 2 6 5 4 together

So,
1 3 2 x x x    together on 4/6 cases

1 3 4 x x x    together all 6/6 cases

1 3 5 2 4 6
1 3 5 2 6 4
1 3 5 4 2 6
1 3 5 4 6 2
1 3 5 6 2 4  together
1 3 5 6 4 2  together

1 3 6 2 4 5
1 3 6 2 5 4
1 3 6 4 2 5
1 3 6 4 5 2
1 3 6 5 2 4 together  
1 3 6 5 4 2 together

So, for

1 3 x x x x  together 14/24 cases 

1 4, 1 5 , and 1 6 should be the same as 1 3.
They are all cases where the first two people
are from different couples.

So,
P(together) = 24/24 + 4*(14/24) = 40/60 = 2/3
P(not-together) = 1/3 for the three couple case, same as the two couple case.

This looks like a pattern.
Let's run a python simulation to see if P(not-together) = 1/3 for the 
five couple case.

"""

import random
import math
import pdb

def checkfortogether(sequence):

    lastnumber = -100
    for number in sequence:
        print number
    return False
        
print checkfortogether([1,2,3,4])