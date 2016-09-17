"""
from http://fivethirtyeight.com/features/how-high-can-count-von-count-count/

You are one of 30 team owners in a professional sports league. In the past, 
your league set the order for its annual draft using the teams records from 
the previous season the team with the worst record got the first draft pick, 
the team with the second-worst record got the next pick, and so on. However, 
due to concerns about teams intentionally losing games to improve their picks, 
the league adopts a modified system. This year, each team tosses a coin. All 
the teams that call their coin toss correctly go into Group A, and the teams 
that lost the toss go into Group B. All the Group A teams pick before all the 
Group B teams; within each group, picks are ordered in the traditional way, 
from worst record to best. If your team would have picked 10th in the old 
system, what is your expected draft position under the new system?


You have a 50-50 chance of drafting in Group A or Group B

If you are in Group A, then there are 9 teams that could draft in 
front of you.  There is a 50% change of each team being in group A.
So on average, 4.5 teams will draft ahead of you, giving your team
an average draft position of 5.5

If you are in Group B, then teams 1-9 will always draft ahead of you.
There is a 50% change that teams 11-30 will draft ahead of you.
On average, 10 of these team will draft ahead of you.
So the average draft position will by 9+10+1 = 20

The overall expected draft position will be the average of these two

0.5(5.5+20) = 12.75

Now, let's try the pythonic solution:

"""

import random
import math
import pdb


def runonesimulation():


    rounda = []
    roundb = []
    
    # seed the round
    for i in range(1,31):
        #print i
        if random.choice([True, False]):
            rounda.append(i)
        else:
            roundb.append(i)
    
    #print rounda
    #print roundb
    
    i = 1
    for entry in rounda:
        if entry == 10: return i
        i += 1
    for entry in roundb:
        if entry == 10: return i    
        i += 1

       
def runmanygames(count):
    total = 0
    for x in range (0,count):
        total  += runonesimulation()
        
    return total, count, float(total)/count        
    

print runmanygames(500000)

"""

Which yields


(6375581, 500000, 12.751162)

(6381706, 500000, 12.763412)

(6375346, 500000, 12.750692)

Thus confirming the 12.75

"""