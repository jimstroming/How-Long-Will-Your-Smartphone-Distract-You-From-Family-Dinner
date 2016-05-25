"""
From http://fivethirtyeight.com/features/can-you-slay-the-puzzle-of-the-monsters-gems/

A video game requires you to slay monsters to collect gems. Every time you slay a monster, 
it drops one of three types of gems: a common gem, an uncommon gem or a rare gem. 
The probabilities of these gems being dropped are in the ratio of 3 to 2 to 1. Three common 
gems for every two uncommon gems for every one rare gem, on average. If you slay monsters
until you have at least one of each of the three types of gems, how many of the most 
common gems will you end up with, on average?
"""


"""
Let's write a python simulation.  
Python simulation shows 3.65 average number of common gem.

"""

import random

def findgems():

    probgems   = [0,0,0,1,1,2]
    numbergems = [0, 0, 0]
    
    while (numbergems[0]*numbergems[1]*numbergems[2] == 0):
        gem = random.choice(probgems)  
        numbergems[gem] += 1

    return numbergems[0]


loopcount = 100000
sum = 0
for x in range(0, loopcount):
    sum += findgems()
print float(sum)/loopcount

"""
probabilities of gems
common   = 1/2 
uncommon = 1/3 
rare     = 1/6


There are 6, length 3 solutions
CUR 1 common, p = 1/36, e = 1/36
CRU 1 common, p = 1/36, e = 1/36
UCR 1 common, p = 1/36, e = 1/36
URC 1 common, p = 1/36, e = 1/36
RCU 1 common, p = 1/36, e = 1/36
RUC 1 common, p = 1/36, e = 1/36
total expected value      = 1/6   for length 3 solutions

CCUR 2 common, p = 1/72, e = 1/36
CCRU 2 common, p = 1/72, e = 1/36
CUCR 2 common, p = 1/72, e = 1/36 
CRCU 2 common, p = 1/72, e = 1/36
UCCR 2 common, p = 1/72, e = 1/36
RCCU 2 common, p = 1/72, e = 1/36

CUUR 1 common, p = 1/108, e = 1/108
UCUR 1 common, p = 1/108, e = 1/108
UUCR 1 common, p = 1/108, e = 1/108
UURC 1 common, p = 1/108, e = 1/108
URUC 1 common, p = 1/108, e = 1/108
RUUC 1 common, p = 1/108, e = 1/108

CRRU 1 common, p = 1/216, e = 1/216
RRUC 1 common, p = 1/216, e = 1/216
URRC 1 common, p = 1/216, e = 1/216
RCRU 1 common, p = 1/216, e = 1/216
RURC 1 common, p = 1/216, e = 1/216
RRCU 1 common, p = 1/216, e = 1/216

CCCC
CCCU
CCCR

CCUC
CCUU

CCRC
CCRR

CUCC
CUCU

CUUC
CUUU

CRCC
CRCR

CRRC
CRRR

UCCC
UCCU

UCUC
UCUU

UUCC
UUCU

UUUC
UUUR
UUUU

UURR
UURU

URUR
URUU

URRR
URRU

RCCC
RCCR

RCRC
RCRR

RUUR
RUUU

RURR
RURU

RRCC
RRCR

RRUR
RRUU

RRRC
RRRR
RRRU

"""

"""
Too brute force.

Let's try to simplify. 
What if we only consider cases that end in R.
By substituting gems, we should be able to change these into cases that end in C and 
into cases that end in U.

CUR
UCR

CCUR
CUCR
CUUR
UCCR
UCUR
UUCR

CCCUR
CCUCR
CCUUR
CUCCR
CUCUR
CUUCR
CUUUR
UCCCR
UCCUR
UCUCR
UCUUR
UUCCR
UUCUR
UUUCR

"""

"""

Simplify again.
Cases that start with C, end in R.


CUR   p = 1/36   E(C) = 1/36   E(U) = 1/36   E(R) = 1/36 

CCUR  p = 1/72   E(C) = 1/36   E(U) = 1/72   E(R) = 1/72
CUCR  p = 1/72   E(C) = 1/36   E(U) = 1/72   E(R) = 1/72
CUUR  p = 1/108  E(C) = 1/108  E(U) = 1/54   E(R) = 1/108


CCCUR p = 1/144  E(C) = 3/144  E(U) = 1/144  E(R) = 1/144
CCUCR p = 1/144  E(C) = 3/144  E(U) = 1/144  E(R) = 1/144
CCUUR p = 1/216  E(C) = 2/216  E(U) = 1/108  E(R) = 1/216
CUCCR p = 1/144  E(C) = 3/144  E(U) = 1/144  E(R) = 1/144
CUCUR p = 1/216  E(C) = 2/216  E(U) = 1/108  E(R) = 1/216
CUUCR p = 1/216  E(C) = 2/216  E(U) = 1/108  E(R) = 1/216
CUUUR p = 1/324  E(C) = 1/324  E(U) = 1/108  E(R) = 1/324 

E(C) = 1/36  + (2/36  + 1/108) + (27/144 + 6/216 + 1/324) +...
     = 1/36  + 5/108  + (27*18 + 6*12 + 6)/(324*6) +...
     = 3/108 + 5/108  + (27*3 +12 +1)/324 +...
     = 3/108 + 5/108  + 94/324 +...
     = 9/324 + 15/342 + 94/324 +...

"""
"""
Another way to look at the case that stars with C and end in R.
It is all the U and C combinations, except for all C.
So let's calculate the total include all C, then subtract out all C.

CCR   p = 1/24   E(C) = 1/12   
CUR   p = 1/36   E(C) = 1/36   


CCCR  p = 1/48   E(C) = 1/16
CCUR  p = 1/72   E(C) = 1/36   
CUCR  p = 1/72   E(C) = 1/36   
CUUR  p = 1/108  E(C) = 1/108  


CCCCR p = 1/96   E(C) = 4/96
CCCUR p = 1/144  E(C) = 3/144  E(U) = 1/144  E(R) = 1/144
CCUCR p = 1/144  E(C) = 3/144  E(U) = 1/144  E(R) = 1/144
CCUUR p = 1/216  E(C) = 2/216  E(U) = 1/108  E(R) = 1/216
CUCCR p = 1/144  E(C) = 3/144  E(U) = 1/144  E(R) = 1/144
CUCUR p = 1/216  E(C) = 2/216  E(U) = 1/108  E(R) = 1/216
CUUCR p = 1/216  E(C) = 2/216  E(U) = 1/108  E(R) = 1/216
CUUUR p = 1/324  E(C) = 1/324  E(U) = 1/108  E(R) = 1/324 


CCCCCR p = 1/192, E(C) = 5/192
CCCCUR p = 1/288, E(C) = 4/288
CCCUCR p = 1/288, E(C) = 4/288
CCCUUR p = 1/432, E(C) = 3/432
CCUCCR p = 1/288, E(C) = 4/288
CCUCUR p = 1/432, E(C) = 3/432
CCUUCR p = 1/432, E(C) = 3/432
CCUUUR p = 1/648, E(C) = 2/648
CUCCCR p = 1/288, E(C) = 4/288
CUCCUR p = 1/432, E(C) = 3/432
CUCUCR p = 1/432, E(C) = 3/432
CUCUUR p = 1/648, E(C) = 2/648
CUUCCR p = 1/432, E(C) = 3/432
CUUCUR p = 1/648, E(C) = 2/648
CUUUCR p = 1/648, E(C) = 2/648
CUUUUR p = 1/972, E(C) = 1/972


CCCCCCR p = 1/384, E(C) = 6/384
CCCCCUR p = 1/576, E(C) = 5/576
CCCCUCR p = 1/576, E(C) = 5/576
CCCCUUR p = 1/864, E(C) = 4/864
CCCUCCR p = 1/576, E(C) = 5/576
CCCUCUR p = 1/864, E(C) = 4/864
CCCUUCR p = 1/864, E(C) = 4/864
CCCUUUR p = 1/1296, E(C) = 3/1296
CCUCCCR p = 1/576, E(C) = 5/576
CCUCCUR p = 1/864, E(C) = 4/864
CCUCUCR p = 1/864, E(C) = 4/864
CCUCUUR p = 1/1296, E(C) = 3/1296
CCUUCCR p = 1/864, E(C) = 4/864
CCUUCUR p = 1/1296, E(C) = 3/1296
CCUUUCR p = 1/1296, E(C) = 3/1296
CCUUUUR p = 1/1944, E(C) = 2/1944
CUCCCCR p = 1/576, E(C) = 5/576
CUCCCUR p = 1/864, E(C) = 4/864
CUCCUCR p = 1/864, E(C) = 4/864
CUCCUUR p = 1/1296, E(C) = 3/1296
CUCUCCR p = 1/864, E(C) = 4/864
CUCUCUR p = 1/1296, E(C) = 3/1296
CUCUUCR p = 1/1296, E(C) = 3/1296
CUCUUUR p = 1/1944, E(C) = 2/1944
CUUCCCR p = 1/864, E(C) = 4/864
CUUCCUR p = 1/1296, E(C) = 3/1296
CUUCUCR p = 1/1296, E(C) = 3/1296
CUUCUUR p = 1/1944, E(C) = 2/1944
CUUUCCR p = 1/1296, E(C) = 3/1296
CUUUCUR p = 1/1944, E(C) = 2/1944
CUUUUCR p = 1/1944, E(C) = 2/1944
CUUUUUR p = 1/2916, E(C) = 1/2916

-------------------------------------

CCCCCCCR p = 1/768,  E(C) = 7/768
CCCCCCUR p = 1/1152, E(C) = 6/1152
CCCCCUCR p = 1/1152, E(C) = 6/1152
CCCCCUUR p = 1/1728, E(C) = 5/1728
CCCCUCCR p = 1/1152, E(C) = 6/1152
CCCCUCUR p = 1/1728, E(C) = 5/1728
CCCCUUCR p = 1/1728, E(C) = 5/1728
CCCCUUUR p = 1/2592, E(C) = 4/2592
CCCUCCCR p = 1/1152, E(C) = 6/1152
CCCUCCUR p = 1/1728, E(C) = 5/1728
CCCUCUCR p = 1/1728, E(C) = 5/1728
CCCUCUUR p = 1/2592, E(C) = 4/2592
CCCUUCCR p = 1/1728, E(C) = 5/1728
CCCUUCUR p = 1/2592, E(C) = 4/2592
CCCUUUCR p = 1/2592, E(C) = 4/2592
CCCUUUUR p = 1/3888, E(C) = 3/3888

CCUCCCCR p = 1/1152, E(C) = 6/1152
CCUCCCUR p = 1/1728, E(C) = 5/1728
CCUCCUCR p = 1/1728, E(C) = 5/1728
CCUCCUUR p = 1/2592, E(C) = 4/2592
CCUCUCCR p = 1/1728, E(C) = 5/1728
CCUCUCUR p = 1/2592, E(C) = 4/2592
CCUCUUCR p = 1/2592, E(C) = 4/2592
CCUCUUUR p = 1/3888, E(C) = 3/3888
CCUUCCCR p = 1/1728, E(C) = 5/1728
CCUUCCUR p = 1/2592, E(C) = 4/2592
CCUUCUCR p = 1/2592, E(C) = 4/2592
CCUUCUUR p = 1/3888, E(C) = 3/3888
CCUUUCCR p = 1/2592, E(C) = 4/2592
CCUUUCUR p = 1/3888, E(C) = 3/3888
CCUUUUCR p = 1/3888, E(C) = 3/3888
CCUUUUUR p = 1/5832, E(C) = 2/5832

CUCCCCCR p = 1/1152, E(C) = 6/1152
CUCCCCUR p = 1/1728, E(C) = 5/1728
CUCCCUCR p = 1/1728, E(C) = 5/1728
CUCCCUUR p = 1/2592, E(C) = 4/2592
CUCCUCCR p = 1/1728, E(C) = 5/1728
CUCCUCUR p = 1/2592, E(C) = 4/2592
CUCCUUCR p = 1/2592, E(C) = 4/2592
CUCCUUUR p = 1/3888, E(C) = 3/3888
CUCUCCCR p = 1/2592, E(C) = 4/2592
CUCUCCUR p = 1/2592, E(C) = 4/2592
CUCUCUCR p = 1/2592, E(C) = 4/2592
CUCUCUUR p = 1/3888, E(C) = 3/3888
CUCUUCCR p = 1/3888, E(C) = 3/3888
CUCUUCUR p = 1/3888, E(C) = 3/3888
CUCUUUCR p = 1/3888, E(C) = 3/3888
CUCUUUUR p = 1/5832, E(C) = 2/5832

CUUCCCCR p = 1/1728, E(C) = 5/1728
CUUCCCUR p = 1/2592, E(C) = 4/2592
CUUCCUCR p = 1/2592, E(C) = 4/2592
CUUCCUUR p = 1/3888, E(C) = 3/3888
CUUCUCCR p = 1/2592, E(C) = 4/2592
CUUCUCUR p = 1/3888, E(C) = 3/3888
CUUCUUCR p = 1/3888, E(C) = 3/3888
CUUCUUUR p = 1/5832, E(C) = 2/5832
CUUUCCCR p = 1/2592, E(C) = 4/2592
CUUUCCUR p = 1/3888, E(C) = 3/3888
CUUUCUCR p = 1/3888, E(C) = 3/3888
CUUUCUUR p = 1/5832, E(C) = 2/5832
CUUUUCCR p = 1/3888, E(C) = 3/3888
CUUUUCUR p = 1/5832, E(C) = 2/5832
CUUUUUCR p = 1/5832, E(C) = 2/5832
CUUUUUUR p = 1/8748, E(C) = 1/8748

Start with the all C combinations.  Are those easy to calculate? Yes
E(C) = 2/24 + 3/48 + 4/96 + ...
     = 1/24 + 1/48 + 1/96 + ...
     + 1/24 + 1/48 + 1/96 + ...
     +        1/48 + 1/96 + ...
     +               1/96 + ...
     = 1/12 + 1/12 + 1/24 + 1/48 + ...
     = 1/12 + 2/12 = 3/12 
     = 1/4
     
Now, the total including all C.

E(C) = 4/36   + (1/16 + 1/18 + 1/108) + (4/96 + 9/144 + 8/216 + 1/324)
     = 1/9    + (27+24+4)/432 +
     = 1/9    + 55/432 +
     = 48/432 + 55/432 +

break it down into manageable units
We will sum the left branches, the right branches, and the center branch

E(C) =                             2/24           + 1/36
                           + 3/48        + 4/72            + 1/108
                     + 4/96         9/144          + 6/216            + 1/324
              + 5/192 +    16/288       + 18/432           + 8/648           + 1/972
        + 6/384 +     25/576 +    40/864 +          30/1296 +         10/1944         + 1/2916
+7/768  +      +36/1152   + 60/1728     + 80/2592             /3888             /5832            +1/8748 
     
= 1/4   +                                                                        + 1/12
"""


"""
Another simplification.
Lets do a case with gem A,B, and C,
where P(A)=P(B)=P(C)=1/3
Cases starting with A, ending with C

A B   C   p = 1/9    E(B) = 1/9

A AB  C   p = 1/27   E(B) = 1/27
A BA  C   p = 1/27   E(B) = 1/27 

A AAB C   p = 1/81   E(B) = 1/81
A ABA C   p = 1/81   E(B) = 1/81 
A ABB C   p = 1/81   E(B) = 2/81
A BAA C   p = 1/81   E(B) = 1/81
A BAB C   p = 1/81   E(B) = 2/81
A BBA C   p = 1/81   E(B) = 2/81

A AAAB C  p = 1/243  E(B) = 1/243
A AABA C  p = 1/243  E(B) = 1/243
A AABB C  p = 1/243  E(B) = 2/243
A ABAA C  p = 1/243  E(B) = 1/243
A ABAB C  p = 1/243  E(B) = 2/243
A ABBA C  p = 1/243  E(B) = 2/243
A ABBB C  p = 1/243  E(B) = 3/243
A BAAA C  p = 1/243  E(B) = 1/243
A BAAB C  p = 1/243  E(B) = 2/243
A BABA C  p = 1/243  E(B) = 2/243
A BABB C  p = 1/243  E(B) = 3/243
A BBAA C  p = 1/243  E(B) = 2/243
A BBAB C  p = 1/243  E(B) = 3/243
A BBBA C  p = 1/243  E(B) = 3/243
A BBBB C  p = 1/243  E(B) = 4/243
Total				 E(B) = (4 + 12 + 12 + 4)/243 = 32/243


So, for cases starting with A, ending with C
E(B) = 1/9  +  2*(1/27)  +  9*(1/81) + 32*(1/243)

"""
"""

Another simplification.  
Let's do a case with gem A and B
where P(A) = P(B) = 1/2
Cases starting with A, ending with B

AB     p = 1/4,  e(A) = 1/4,  e(B) = 1/4
AAB    p = 1/8,  e(A) = 1/4,  e(B) = 1/8
AAAB   p = 1/16, e(A) = 3/16, e(B) = 1/16
AAAAB  p = 1/32, e(A) = 4/32, e(B) = 1/32

Cases starting with B, ending with A

                 e(B) = 1/4,  e(A) = 1/4
                 e(B) = 2/8,  e(A) = 1/8
                 e(B) = 3/16, e(A) = 1/16
                 e(B) = 4/32, e(A) = 1/32
                 
e(A) = 1/4+1/8+1/16+1/32+...
     + 1/4+2/8+3/16+4/32+...
     
for the first sequence     
S = a/(1-r)
  = (1/4)(1-1/2) = 1/2                     

for the 2nd sequence
1/4 + 2/8 + 3/16 + 4/32 
=

1/4 + 1/8 + 1/16 + 1/32 + ...     = 1/2
+
      1/8 + 1/16 + 1/32 + ...     = 1/4
+      
            1/16 + 1/32 + ...     = 1/8
...

So the 2nd sequence = 

1/2 + 1/4 + 1/8 =  1

So, e(A) = 1/2 + 1 = 1.5 = e(B)
            


# Let's validate the two gem case with python

"""

def findtwogems():

    probgems   = [0,1]
    numbergems = [0,0]

    while (numbergems[0]*numbergems[1] == 0):
        gem = random.choice(probgems)
        numbergems[gem] += 1

    return numbergems[0]

"""
# Another simplified case.
p(A) = 1/3, p(B) = 2/3
Find expected number of B to till you get both A and B

Cases starting with A, ending with B

AB     p = 2/9,   e(A) = 2/9,   e(B) = 2/9
AAB    p = 2/27,  e(A) = 4/27,  e(B) = 2/27
AAAB   p = 2/81,  e(A) = 6/81,  e(B) = 2/81
AAAAB  p = 2/243, e(A) = 8/243, e(B) = 2/243

Cases starting with B, ending with A

BA     p = 2/9    e(A) = 2/9    e(B) = 2/9
BBA    p = 4/27   e(A) = 4/27   e(B) = 8/27
BBBA   p = 8/81   e(A) = 8/81   e(B) = 24/81
BBBBA  p = 16/243 e(A) = 16/243 e(B) = 64/243


For cases starting with A,
e(A) = 2/9 + 4/27 + 6/81 + 8/243 + ...
     = 2/9 + 2/27 + 2/81 + 2/243 + ...
     +       2/27 + 2/81 + 2/243 + ...
     +              2/81 + 2/243 + ...
     = a/(1-r) 
     = 3/9 + 3/27 + 3/81  + 3/243
     = (3/9)(1-1/3) = (3/9)/(2/3) = 1/2
e(B) = 2/9 + 2/27 + 2/81 + 2/243 + ...
    = (2/9)/(1-1/3) = 1/3 
 
For cases starting with B,
e(A) = 2/9 + 4/27 + 8/81 + 16/243 + ...
     = (2/9)/(1-2/3) = 2/3
e(B) = 2/9 + 8/27 + 24/81 + 64/243     
     = 2/9 + 4/27 +  8/81 + 16/243 + ...
     +       4/27 +  8/81 + 16/243 + ...
     +               8/81 + 16/243 + ...
     
     = (2/9)/(1/3) + (4/27)/(1/3) + (8/81)/(1/3) + ...
     = 3(2/9)/(1-2/3) = 2
So, in total
e(A) = 1/2 + 2/3 = 7/6  = 1.17
e(B) = 1/3 + 2   = 7/3  = 2.33
                              
"""
# Now, lets simulate the 2 gem, uneven probability case

def findtwogemsuneven():

    probgems   = [0,1,1]
    numbergems = [0,0]

    while (numbergems[0]*numbergems[1] == 0):
        gem = random.choice(probgems)
        numbergems[gem] += 1

    return numbergems[0], numbergems[1]


loopcount = 20000
sum0 = sum1 = 0
for x in range(0, loopcount):
    gem0,gem1 = findtwogemsuneven()
    sum0 += gem0
    sum1 += gem1
print float(sum0)/loopcount
print float(sum1)/loopcount

