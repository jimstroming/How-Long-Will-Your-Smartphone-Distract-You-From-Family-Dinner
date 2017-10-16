"""
from https://fivethirtyeight.com/features/how-much-is-a-perfect-game-of-jeopardy-worth/

Austin Rodgers is having quite a run on the game show Jeopardy. As The Riddler 
goes to press, he has won $411,000 over 12 days. What is the maximum amount of 
money that can possibly be won by one contestant in a single game of Jeopardy

"""  

def simulateround(startingdollars, numbcategories, numbrows, lowdollar, highdollar, numdailydoubles):

  # add up the total dollar amount of the board
  totaldollars =  startingdollars
  print totaldollars
  totaldollars += numbcategories*numbrows*(highdollar + lowdollar)/2 
  print totaldollars
  # subtract out the lower dollar amount for the daily doubles, since
  # those will be the daily double, instead
  totaldollars -= numdailydoubles*lowdollar
  print totaldollars
  # double the dollar amount for each daily double.
  totaldollars = totaldollars * 2**numdailydoubles
  print totaldollars
  return totaldollars
  
  
def simulategame():

  firstroundtotal =  simulateround(0, 6, 5, 100, 500, 1)
  print "After the first round, you can have ", firstroundtotal
  secondroundtotal = simulateround(firstroundtotal, 6, 5, 200, 1000, 2)  
  print "After the second round, you can have ", secondroundtotal
  finalscore =  secondroundtotal * 2
  print "At the end of the game, you can have",  finalscore
  return finalscore
  
simulategame() 

"""
So 283,200 dollars is the most you can win.
"""