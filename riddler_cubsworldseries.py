"""
from fivethirtyeight.com
http://fivethirtyeight.com/features/cubs-world-series-puzzles-for-fun-and-profit/

You are a gambler and a Cubs fan. The Cubs are competing in a seven-game series 
against the Red Sox, first to four games wins. Your bookie agrees to take any 
even odds bets on any of the individual games. Can you construct a series of 
bets such that the guaranteed outcomes are You win 100 dollars if the Cubs wins 
the series and lose 100 if the Red Sox win it?
"""

""""
A great problem.  Go Cubs!  Though I'm afraid, in real life, something
horrible will happen in Game 7.  But, back to the problem. 

The key is to start backwards and work our way forward.

Let's start with game 7.
If we get to game 7, then we must be even on our betting outcomes to this point.
If the Cubs win game 7, we must end up $100 ahead.
If they lose, we must end up $100 behind.
So the wager on game 7 must be $100, and the initial condition entering 
game 7 must have been we were dead even.

Now let's do game 6.
Entering game 6, one team will be ahead 3-2.
Let's say the Cubs are up 3-2.
If the Cubs win game 6, then we must end up $100 up, since the Series is over
If the Cubs lose game 6, then we must end up even, since the Series is tied
heading to a game 7.
So the game 6 wager must be $50, and we must be up $50 heading into game 6 
if the Cubs are up 3-2, or down $50 if the Cubs are down 2-3.

On to game 5.
Game 5 has a couple different possibilities:
The series could be ties 2-2, or one team could be ahead 3-1.

If the series is tied 2-2, then we currently must be even in our winnings.
If the Cubs win, then we must end up at the game 6 initial condition of up $50.
If the Cubs lose, we most be down $50.
So if the series is tied 2-2, we wager $50 on game 6.

If the Cubs are up 3-1 entering game 5, then if the cubs win, we must have $100.
If the Cubs lose, then we must be at the game 6 initial condition of up $50.
So if the series is 3-1, we wager $25, and we must have had $75 going into game
5 is the Cubs were up 3-1.

Game 4 has two different initial conditions:  3-0 or 2-1.
If the Cubs are up 3-0 and win game 4, then we must be up $100.
If the Cubs are up 3-0 and lose, we must be up $75.
So if the series is 3-0, we wager $12.50, and we are either up or down $87.50 
going into the game.

If the Cubs are up 2-1 and win game 4, then we must be up $75.
If the Cubs lose, then we are tied and even.
So the wager must be $37.50, and we were up or down $37.50 entering the game.


Entering game 3, the score is either 2-0 or 1-1.
If the Cubs are up 2-0 and win game 3, then we must be up $87.50
If the Cubs lose, then we go up $37.50.
So the wager must be $25, and we were up or down $62.50 going in.

If the score is tied 1-1, then we must be even going into the game.
If the Cubs win, we go up $37.50.
If the Cubs lose, we go down $37.50
So the wager must be $37.50.

Getting closer now.  On to game 2.
In game 2, one team is up 1-0.
If the Cubs are up 1-0 and win game 1, we must go up $62.50.
If the Cubs are up 1-0 and lose, we must be even.
So the wager must be $31.25, and we were up or down $31.25 going in.





"""

import sys
import random


 
