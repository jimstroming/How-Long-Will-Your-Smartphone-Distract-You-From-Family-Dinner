"""
from http://fivethirtyeight.com/features/can-you-solve-the-puzzle-of-the-baseball-division-champs/

Assume you have a sport (lets call it baseball) in which each team plays 162 games in 
a season. Assume you have a division of five teams (call it the AL East) where each 
team is of exact equal ability. Specifically, each team has a 50 percent chance of 
winning each game. What is the expected value of the number of wins for the team that
finishes in first place?

"""

"""

Need to make an assumption about interdivision vs intradivision games.
Lets start with the way the schedule is done currently.
19 games against each of your 4 division opponents.
86 games outside your division.

"""

import random
import pdb

def simulateseason(numberteams, winningpercentage, intradivisionperteam, outsidedivision):

    
    # construct the winsperteam list
    winsperteam = []
    for x in range (0,numberteams):
        winsperteam.append(0)    
    
    
    
    # play the interdivision games
    
    for teamnumber in range (0, numberteams):
        for x in range (0, outsidedivision):
            if random.random() > winningpercentage:
                winsperteam[teamnumber] += 1
    
    # play the intradivision games
    
    
    
    return winsperteam


numberteams = 5
winningpercentage = .5
intradivisionperteam = 19
outsidedivision = 86

result = simulateseason(numberteams, winningpercentage, intradivisionperteam, outsidedivision)
pdb.set_trace() 

