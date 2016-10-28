"""
Rig The Election ... With Math!
From the 538 riddler
http://fivethirtyeight.com/features/rig-the-election-with-math/

First, in Riddler Express, learn how to gerrymander:

Imagine your job is to draw districts and you happen to be a member 
of the Blue Party. The grid below gives the locations of 25 voters in a 
region, which you must divide into five districts with five voters each. 
In each district, the party with the most votes will win. The districts must 
be non-overlapping and contiguous (that is, each square in a district must 
share an edge with at least one other square in the district). Can you draw 
the districts such that the Blue Party wins more districts than the Red Party?

B  B  r  r  r

r  B  B  r  B

B  r  r  r  r

r  r  B  B  r

r  r  r  r  B


Now, in Riddler Classic, gerrymander a whole state!

In the real world, of course, there arent just 25 voters. Even if you can 
group neighborhoods together, the grid of voters in an entire state is going 
to be much larger, meaning that a computer program will probably be necessary 
to optimally gerrymander. Below is a rough approximation of Colorados voter 
preferences, based on county-level results from the 2012 presidential election, 
in a 14-by-10 grid. Colorado has seven districts, so each would have 20 voters 
in this model. What is the most districts that the Red Party could win if you 
get to draw the districts with the same rules as above? What about the 
Blue Party? (Assume ties within a district are considered wins for the party 
of your choice.)

r  r  r  r  B  r  B  B  r  r  r  r  r  r
r  r  r  B  B  r  B  B  r  r  r  r  r  r
r  r  r  r  B  r  r  B  B  B  r  r  r  r
r  r  r  r  B  B  B  B  B  B  r  r  r  r
r  r  r  B  B  B  r  r  r  r  r  r  r  r
r  r  r  B  B  r  r  r  r  r  r  r  r  r
r  r  r  B  B  B  r  r  B  B  r  r  r  r
B  B  B  r  B  B  B  r  B  B  r  r  r  r 
r  r  B  r  r  r  B  B  B  B  B  B  r  r
r  B  B  r  r  B  B  B  B  B  B  B  r  r


"""

"""

Lets start with the simpler Riddler express problem, first.
There are 9 blue squares and 16 red squares.
For blue to win the election, we need blue to win 3 of the 
districts 3 to 2.  Red wins the other 2 districts 5 to 0.
One possible districting is below

---------------
|B  B |r  r  r |
|   -----   ---|
|r |B  B |r |B |
|  |     |  |  |
|B |r  r |r |r |
|  |--   |--   |
|r |r |B |B  r |
---   ------   |
|r  r  r  r |B |
-----------------
