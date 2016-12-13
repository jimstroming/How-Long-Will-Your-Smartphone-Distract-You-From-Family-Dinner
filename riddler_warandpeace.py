"""
from
http://fivethirtyeight.com/features/how-much-gold-would-push-you-into-a-war/

A game theory puzzle from Juan Carrillo that indulges in international diplomacy:

Consider the following war game: Two countries are eyeing each others gold. 
At the beginning of the game, the strength of each countrys army is drawn 
from a continuous uniform distribution and lies somewhere between 0 
(very weak) and 1 (very strong). Each country knows its own strength but not 
that of its opponent. The countries observe their own strength and then 
simultaneously announce peace or war.

If both announce peace, then they each stay quietly in their own territory, 
with their own gold, which is worth $1 trillion (so each wins $1 trillion).

If at least one announces war, then they go to war, and the country with the 
stronger army wins the others gold. (That is, the stronger country wins $2 
trillion, and the other wins $0.)

What is the optimal strategy of each country (declaring peace or war) given 
its strength?

"""

"""


Let's say my army has a strength of 0.
I will lose any fight.
So I will not fight, but my opponent doesn't know that.

If my opponent also has a strength of 0, she will also not fight.
So we each keep the $1 trillion.

If my opponent has a strength of 1, she will definitely fight.
So she will get $2 trillion, and I will get $0.

----

Let's say my army has a strength of 1.
I will lose win any fight.
So, I will fight, but my opponent doesn't know that.

If my opponent has a strength of 0, she will not fight.
So I will get $2 trillion, and she will get $0

If my opponent has a strength of 1, she will fight.
We fight to a draw, and each get $1 trillion.

----





