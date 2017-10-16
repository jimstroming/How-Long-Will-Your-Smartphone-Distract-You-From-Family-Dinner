"""
from https://fivethirtyeight.com/features/how-much-is-a-perfect-game-of-jeopardy-worth/

Austin Rodgers is having quite a run on the game show Jeopardy. As The Riddler 
goes to press, he has won $411,000 over 12 days. What is the maximum amount of 
money that can possibly be won by one contestant in a single game of Jeopardy

"""  

def simulateround(startingdollars, numbcategories, numbrows, lowdollar, highdollar, numdailydoubles):

  # add up the total dollar amount of the board
  totaldollars =  startingdollars
  totaldollars += numbcategories*numbrows*(highdollar + lowdollar)/2 
  
  # subtract out the lower dollar amount for the daily doubles, since
  # those will be the daily double, instead
  totaldollars -= numdailydoubles*lowdollar

  # double the dollar amount for each daily double.
  totaldollars = totaldollars * 2^numdailydoubles
  
  return totaldollars
  
print simulateround(0, 6, 5, 100, 500, 0)  