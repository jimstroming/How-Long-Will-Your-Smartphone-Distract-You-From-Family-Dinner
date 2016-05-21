"""
From http://fivethirtyeight.com/features/can-you-slay-the-puzzle-of-the-monsters-gems/

A video game requires you to slay monsters to collect gems. Every time you slay a monster, 
it drops one of three types of gems: a common gem, an uncommon gem or a rare gem. 
The probabilities of these gems being dropped are in the ratio of 3:2:1 — three common 
gems for every two uncommon gems for every one rare gem, on average. If you slay monsters 
until you have at least one of each of the three types of gems, how many of the most 
common gems will you end up with, on average?
"""

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