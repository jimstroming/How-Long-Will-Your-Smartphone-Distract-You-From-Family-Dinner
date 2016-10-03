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

 






"""

import sys
import random


 
