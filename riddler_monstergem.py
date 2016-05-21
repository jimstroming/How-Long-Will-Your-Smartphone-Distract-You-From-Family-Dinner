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



CCCC
CCCU
CCCR

CCUC
CCUU
CCUR 2 common, p = 1/72, e = 1/36

CCRC
CCRU 2 common, p = 1/72, e = 1/36
CCRR

CUCC
CUCU
CUCR 2 common, p = 1/72, e = 1/36 

CUUC
CUUU
CUUR 1 common, p = 1/108, e = 1/108

CRCC
CRCU 2 common, p = 1/72, e=1/36
CRCR

CRRC
CRRR
CRRU 1 common, p = 1/216, e = 1/216

UCCC
UCCR 2 common, p = 1/72, e = 1/36
UCCU

UCUC
UCUR 1 common, p = 1/108, e = 1/108
UCUU

UUCC
UUCR 1 common, p = 1/108, e = 1/108
UUCU

UUUC
UUUR
UUUU

UURC 1 common, p = 1/108, e = 1/108
UURR
UURU

URUC 1 common, p = 1/108, e = 1/108
URUR
URUU

URRC 1 common, p = 1/216, e = 1/216
URRR
URRU

RCCC
RCCR
RCCU 2 common, p = 1/72, e = 1/36

RCRC
RCRR
RCRU 1 common, p = 1/216, e = 1/216

RUUC 1 common, p = 1/108, e = 1/108
RUUR
RUUU

RURC 1 common, p = 1/216, e = 1/216
RURR
RURU

RRCC
RRCR
RRCU 1 common, p = 1/216, e = 1/216

RRUC 1 common, p = 1/216, e = 1/216
RRUR
RRUU

RRRC
RRRR
RRRU

"""