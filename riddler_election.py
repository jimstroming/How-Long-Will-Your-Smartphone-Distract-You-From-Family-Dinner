"""
from fivethirtyeight.com
http://fivethirtyeight.com/features/a-puzzle-will-you-yes-you-decide-the-election/

You are the only sane voter in a state with two candidates running for Senate. 
There are N other people in the state, and each of them votes completely 
randomly! Those voters all act independently and have a 50-50 chance of voting 
for either candidate. 

What are the odds that your vote changes the outcome of the election toward 
your preferred candidate?

More importantly, how do these odds scale with the number of people in the 
state? For example, if twice as many people lived in the state, how much 
would your chances of swinging the election change?
"""

""""
Let's solve it analytically first, and treat the even and off cases 
differently.

The total number of voters is N+1, since you are not included in N.
If N is even, then for your vote to matter, the vote must be tied
prior to your vote.
If N is odd, then for your vote to matter, your vote must either force
a tie or result in no tie.  So either candidate A is up by one vote, 
or candidate B is up by one vote.  



"""
"""
Let's run a python simulation of these rules to see if they are correct.

"""

import sys
import random

