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

What if I get a strength of 0.2.
This is not a very good strength.  I will probably lose a fight.
There are five possible scenarios.

I fight, opponent strength > 0.2   -> I get $0, 
I fight, opponent strength < 0.2   -> I get $2 trillion
I don't fight, opponent doesn't fight  -> I get $1 trillion
i don't fight, opponent fights, opponent strength > 0.2  -> I get $0
I don't fight, opponent fights, opponent strength < 0.2  -> I get $2 trillion

One thing I can use is that, for the optimal strategy, whatever rule
I adapt, my opponent will also adapt, since we are in the identical situation.

-------------

Let's say both players adopt a rule of never fight.
The expected return will be $1 trillion.

Let's say both players adopt a rule of always fight.
My expected return = $0*P(me having a lower strength)
                  +($2 trillion)*P(me having a higher strength)
          = $0*0.5 +($2 trillion)*0.5 = $1 trillion.
          
Let's say both players adopt a rule of fighting when strength > 0.5
My expected return = $0*P(opp strength > my strength and opp strength >  0.5)
                 +($1 trillion)*P(my strength < 0.5 and opp strength < 0.5)
                 +($2 trillion)*P(my strength > opp strength and my strength > 0.5)

= 0*(3/8) + ($1 trillion)*(0.5)*(0.5) + ($2 trillion)*(3/8)
=  $250 billion + $750 billion = $1 trillion.

Now, let's do the general case.
Both players adopt a rule of fighting when strength > n.

My expected return = $0*P(opp strength > my strength and opp strength > n)
              + ($1 trillion)P(my strength < n and opp strength < n)
              + ($2 trillion)P(my strength > opp strength and my strength > n)
   =  0*(1-n^2)/2 +($1 trillion)*n^2 +($2 trillion)*(1-n^2)/2
   = ($1 trillion)(n^2 + (1-n^2)) = $1 trillion
   
So whatever cutoff point I choose, as long as we both use it, the expected 
return will be $1 trillion.

This is a big problem.  There is no obvious optimal strategy we can both
discover independently and agree upon.  So how do I choose a strategy?

-----

Let's try another approach.  
What if my opponent decides never to fight, and I choose to fight if my
strength > n?  What would my expected return be?

My expected return = $0*P(my strength > n and opp strength > my strength)
         + ($1 trillion)P(my strength < n)
         + ($2 trillion)P(my strength > n and my strength > opp strength)
         
  =  0  +($1 trillion)n  + ($2 trillion)(1-n^2)/2
  = ($1 trillion)(n +(1-n^2))
  = ($1 trillion)(1 + n - n^2)
  
Set the derivative to zero to find a local max/min
0 = 1-2n; n = 0.5

E(0) = $1 trillion
E(1) = $1 trillion
E(0.5) = ($1 trillion)(1 + 0.5 - 0.25) = $1.25 trillion

------------

What is my opponent decides to always fight, and I choose to fight if my 
strength >n?  What would my expected return be?

My expected return = $0*P(opp strength > my strength) 
        + ($2 trillion)P(my strength > opp strength)
      = $1 trillion
      
--------------

What if my opponent decides to fight on strength > .25, and I choose 
to fight if my strength if greater than n?

My expected return = $0*P(opp strength > my strength and (opp strength > .25 or my strength > n)) 
     +($1 trillion)P(opp strength < .25 and my strength < n)    
     +($2 trillion)P(my strength > opp strength and (opp strength > .25 or my strength > n))          


------------------

Let's try the extra credit questions now.
They may give some insight into finishing off the main problem

--------------

Extra credit: What if the value of winning the war were $5 trillion rather than $2 trillion?

Both players adopt a rule of fighting when their strength > n.

My expected return = $0*P(opp strength > my strength and opp strength > n)
              + ($1 trillion)P(my strength < n and opp strength < n)
              + ($5 trillion)P(my strength > opp strength and my strength > n)
   =  0*(1-n^2)/2 +($1 trillion)*n^2 +($5 trillion)*(1-n^2)/2
   = ($1 trillion)(n^2 + 2.5(1-n^2))
   = ($1 trillion)(2.5-1.5(n^2))
   
Set the derivative to zero to find the local min/max
0 = -3n
n = 0

E(0) = 2.5 trillion
E(1) = 1 trillion

So, if the value of winning the war is $5 trillion, then you should always fight.

Is this correct?
What is we set n = 1/2
E(1/2) = ($1 trillion)(2.5-1.5/4) = $2.125 trillion <  $2.5 trillion 
That $5 trillion dollar prize is so great.
If you have a tiny strength, your opponent is probably going to go to war and 
you'll get nothing.  But you are better off going to war just in case they have 
a smaller strength than you, rather than hoping for peace and the smaller prize.



