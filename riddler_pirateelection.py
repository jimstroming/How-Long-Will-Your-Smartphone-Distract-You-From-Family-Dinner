"""
from http://fivethirtyeight.com/features/can-you-solve-the-puzzle-of-the-pirate-booty/

Ten Perfectly Rational Pirate Logicians (PRPLs) find 10 (indivisible) gold pieces and wish
to distribute the booty among themselves.

The pirates each have a unique rank, from the captain on down. The captain puts forth the 
first plan to divide up the gold, whereupon the pirates (including the captain) vote. 
If at least half the pirates vote for the plan, it is enacted, and the gold is distributed
accordingly. If the plan gets fewer than half the votes, however, the captain is killed, 
the second-in-command is promoted, and the process starts over. 
(Theyre mutinous, these PRPLs.)

Pirates always vote by the following rules, with the earliest rule taking precedence 
in a conflict:

Self-preservation: A pirate values his life above all else.
Greed: A pirate seeks as much gold as possible.
Bloodthirst: Failing a threat to his life or bounty, a pirate always votes to kill.
Under this system, how do the PRPLs divide up their gold?

"""

""" 
A few observations:
The low ranking pirates have very little incentive to vote yes 
initially, since, when the game gets down to only a few players,
they will get a lot of gold.

The pirate captain only needs 4 votes besides himself.
He will likely have to try for the 4 highest ranking.

The pirate captain may very well have no hope.

"""

"""
Let's try working backwards.  Start with 1 pirate, then add more.

1 pirate case.
Pirate #10 would get all 10 pieces.

2 pirate case.
Pirate #9 would propose all 10 pieces for himself.
The vote would be a 1-1 tie.  Pirate 9 would get all 10 pieces.
So, Pirate #9 wants the 2 pirate case.  Pirate #10 does not.

3 pirate case.
Pirate #10 will always vote yes in this case, since he needs to avoid the 2 pirate case.
Pirate #9 will always vote no in this case, since she wants the 2 pirate case.
Pirate #8 therefore gives herself all 10 pieces.  
So, pirates #10 and #9 want to avoid the 3 pirate case.





