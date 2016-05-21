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



CCC
CCU
CCR

CUC
CUU

CRC

CRR

UCC
UCU


UUC
UUU
UUR


URU
URR

RCC

RCR


RUU
RUR

RRC
RRU
RRR

"""