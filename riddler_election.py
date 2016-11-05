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

"""
"""
Let's run a python simulation of these rules to see if they are correct.

"""

import sys
import random

