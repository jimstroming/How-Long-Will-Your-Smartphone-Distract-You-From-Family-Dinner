''' 
from http://fivethirtyeight.com/features/can-you-figure-out-how-to-beat-roger-federer-at-wimbledon/

Your wish has been granted, and you get to play tennis against Roger Federer in his prime 
in the Wimbledon final. You have only a 1 percent chance to win each point, but Roger, 
sporting gentleman that he is, offers to let you name any score and begin the match at 
that point. (So, if youve entertained a fantasy of storming back after being down three 
match points in the fifth set, nows the time to live it.) What score can you name that 
gives you the best chance to win, and what is your chance of winning the title

'''

import random
import math
import pdb

'''

Wimbledon men's matches are best of 5 sets.
You win a set by winning 6 games, with a lead of two.
If the 1st through 4th set reaches 7-7, it goes to a tiebreaker.
The 5th set, on the other hand, continues until someone gets
a two game lead.

So, your best shot is to be leading 2 sets to none,
up 5 games to love in the 3rd set, and up 40-0 in the 5th set.

You will now have 3 match points.  Your chance of winning those
three match points is

.01 + (.99)(.01) + (.99)(.99)(.01) = 2.9701 percent

If you lose those 3 match points, your chance of winning plummets.
But we need to calculate to see how much the total chance
is above 2.9701 percent

The analytic calculation is complicated, with the tiebreaker and 
the 5th sent not having the tie breaker.  
Let's solve the pythonic solution.

'''

class TennisMatch(object):

    setswon = [0,0]
    gameswon = [0,0]
    pointswon = [0,0]
    gamepoints = ['0','15','30','40']
    winneroflastpoint = None
    
    def setscore(self, player1sets, player2sets, player1games, player2games, 
                player1points, player2points):
        self.setswon[0] = player1sets
        self.setswon[1] = player2sets
        self.gameswon[0] = player1games
        self.gameswon[1] = player2games
        self.pointswon[0] = player1points
        self.pointswon[1] = player2points

    def checkwhichplayerwon(self):
        if self.setswon[0] == 3:
            return 0
        if self.setswon[1] == 3:
            return 1
    
    
    def incrementscore(self,winner):
        # returns True if the match is over.  False if it continues
        gamewon = False
        setwon = False
        self.pointswon[playerwhowonthepoint] += 1  # add a point to the score
        # check if we are in a tie breaker
        if self.gameswon[0] == 7 and self.gameswon[1] == 7 and self.setswon[0] + self.setswon[1] != 4:
            if (self.pointswon[winner] == 7 and self.pointswon[1-winner]  < 7) or (self.pointswon[winner] > 7 and winneroflastpoint == winner):
                setwon = True
            else:
                winneroflastpoint = winner
        else:
            if (self.pointswon[winner] == 4 and self.pointswon[1-winner] < 4) or (self.pointswon[winner] > 4 and self.pointswon[winner]-self.pointswon[1-winner] > 1):
                gamewon = True
        if gamewon:
            self.pointswon[0] = 0
            self.pointswon[1] = 0
            self.gameswon[winner] += 1
            if self.setswon[winner] > 5 and self.setswon[winner] - self.setswon[1-winner] > 1:
                setwon = True
            elif self.setswon[winner] == 8: setwon = True
        if setwon:
            self.setswon[winner] += 1
            self.gameswon[0] = 0
            self.gameswon[1] = 0
            if setswon[winner] == 3:  return True
        return False
    
    # tie breaker scoring is first to 7 points win, unless the score gets to 6-6
    # if the score gets to 6-6, then the first to win two points in a row wins.

match = TennisMatch()
match.setscore(2,0,5,0,3,0)            