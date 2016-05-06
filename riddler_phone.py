''' 
from fivethirtyeight.com
http://fivethirtyeight.com/features/how-long-will-your-smartphone-distract-you-from-family-dinner/
My solution to the 12/22/2015 riddler
Youve just finished unwrapping your holiday presents. 
You and your sister got brand-new smartphones, opening them at the same moment. 
You immediately both start doing important tasks on the Internet, 
and each task you do takes one to five minutes. 
(All tasks take exactly one, two, three, four or five minutes, with an equal 
probability of each). After each task, you have a brief moment of clarity. 
During these, you remember that you and your sister are supposed to join the rest 
of the family for dinner and that you promised each other youd arrive together. 
You ask if your sister is ready to eat, but if she is still in the middle of a task, 
she asks for time to finish it. In that case, you now have time to kill, so you start a 
new task (again, it will take one, two, three, four or five minutes, exactly, with an 
equal probability of each). If she asks you if its time for dinner while youre still 
busy, you ask for time to finish up and she starts a new task and so on. From the moment 
you first open your gifts, how long on average does it take for both of you to be between 
tasks at the same time so you can finally eat? (You can assume the moments of clarity 
are so brief as to take no measurable time at all.)
'''

import random

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

print averagetimetoeat(100000), "average minutes till you can eat dinner"
