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


CCC
CCU
CCR

CUC
CUU
CUR 1 common

CRC
CRU 1 common
CRR

UCC
UCU
UCR 1 common

UUC
UUU
UUR

URC 1 common
URU
URR

RCC
RCU 1 common
RCR

RUC 1 common
RUU
RUR

RRC
RRU
RRR

"""