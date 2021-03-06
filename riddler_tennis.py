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
ties 6 games to 6 in the 3rd set, and up 6-0 in the tiebreaker.

You will now have 6 match points.  Your chance of winning any one those
six match points is

1-(.99^6) = 5.85%

If you lose those 6 match points, your chance of winning plummets.

The analytic from that point on is complicated, with the tiebreaker and 
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
    
    def printscore(self):
        if (self.gameswon[0] == 6 and self.gameswon[1] == 6) or self.pointswon[0] + self.pointswon[1] > 6:
            print "Player 1: ", self.setswon[0] ," sets, ", self.gameswon[0], "games, ",self.pointswon[0]
            print "Player 2: ", self.setswon[1] ," sets, ", self.gameswon[1], "games, ",self.pointswon[1]       
        else:
            print "Player 1: ", self.setswon[0] ," sets, ", self.gameswon[0], "games, ",self.gamepoints[self.pointswon[0]]
            print "Player 2: ", self.setswon[1] ," sets, ", self.gameswon[1], "games, ",self.gamepoints[self.pointswon[1]]
           
    def incrementscore(self,winner):
        # returns True if the match is over.  False if it continues
        gamewon = False
        setwon = False
        self.pointswon[winner] += 1  # add a point to the score
        # check if we are in a tie breaker
        if self.gameswon[0] == 6 and self.gameswon[1] == 6 and self.setswon[0] + self.setswon[1] != 4:
            if (self.pointswon[winner] >= 7 and self.pointswon[1-winner] < self.pointswon[winner] - 1):
                setwon = True
                self.pointswon[0] = 0
                self.pointswon[1] = 0
        else:
            if (self.pointswon[winner] == 4 and self.pointswon[1-winner] < 3) or (self.pointswon[winner] > 4 and self.pointswon[winner]-self.pointswon[1-winner] > 1):
                gamewon = True
        if gamewon:
            self.pointswon[0] = 0
            self.pointswon[1] = 0
            self.gameswon[winner] += 1
            if self.gameswon[winner] > 5 and self.gameswon[winner] - self.gameswon[1-winner] > 1:
                setwon = True
            elif self.gameswon[winner] == 7: setwon = True
        if setwon:
            self.setswon[winner] += 1
            self.gameswon[0] = 0
            self.gameswon[1] = 0
            if self.setswon[winner] == 3:  return True
        return False
        
    def playrandompoint(self, chanceofplayer0winning):
        # returns True if the match if over.
        if random.random() > chanceofplayer0winning:
            return self.incrementscore(1)
        return self.incrementscore(0)
        
    def playmatch(self, initialscorelist, chanceofplayer0winning):
        # returns 0 if player 0 wins.  Returns 1 if player 1 wins
        x = initialscorelist
        self.setscore(x[0],x[1],x[2],x[3],x[4],x[5])
        matchover = False
        while not matchover:
            matchover = self.playrandompoint(chanceofplayer0winning)
            #self.printscore()
        return self.checkwhichplayerwon()    
            
    def playmanymatches(self, N, initialscorelist, chanceofplayer0winning):
        sum = 0
        for x in range(0,N):
            sum += self.playmatch(initialscorelist, chanceofplayer0winning)
        print sum, N
        return float(sum)/N
    
    # tie breaker scoring is first to 7 points win, unless the score gets to 6-6
    # if the score gets to 6-6, then the first to win two points in a row wins.

match = TennisMatch()
#match.setscore(2,0,5,0,3,0)  
#match.setscore(0,0,6,6,0,0)

print match.playmanymatches(5000000,[0,2,6,6,0,6],0.99)


''' Tried running this with different loop counts



$ python riddler_tennis.py
29302 500000
0.058604
$ python riddler_tennis.py
292821 5000000
0.0585642

So, it looks like the answer is approximately 5.86% .
Bottom line:  Better win one of those 6 match points.  
'''