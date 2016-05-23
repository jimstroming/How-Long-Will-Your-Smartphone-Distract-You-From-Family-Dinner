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

CCCUR
CCUCR
CCUUR
CUCCR
CUCUR
CUUCR
CUUUR  

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

