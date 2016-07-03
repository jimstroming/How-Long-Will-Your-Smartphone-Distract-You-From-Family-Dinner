''' 
from http://fivethirtyeight.com/features/can-you-figure-out-how-to-beat-roger-federer-at-wimbledon/

Your wish has been granted, and you get to play tennis against Roger Federer in his prime 
in the Wimbledon final. You have only a 1 percent chance to win each point, but Roger, 
sporting gentleman that he is, offers to let you name any score and begin the match at 
that point. (So, if youve entertained a fantasy of storming back after being down three 
match points in the fifth set, now’s the time to live it.) What score can you name that 
gives you the best chance to win, and what is your chance of winning the title?

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

1% + (99%)(1%) + (99%)(99%)(1%) = 2.9701 %

If you lose those 3 match points, your chance of winning plummets.
But we need to calculate to see how much the total chance
is above 2.9701 %

The analytic calculation is complicated, with the tiebreaker and 
the 5th sent not having the tie breaker.  
Let's solve the pythonic solution.

'''

