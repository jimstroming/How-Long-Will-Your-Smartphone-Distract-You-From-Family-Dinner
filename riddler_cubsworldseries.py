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
 






"""

import sys
import random


 
