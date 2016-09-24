"""
From Project Euler
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

maxlimit = 1000
flags = [False]*maxlimit

sum = 0
for i in range(0,maxlimit,3):
    flags[i] = True
    sum += i
  
for i in range(0,maxlimit,5):
    if not flags[i]: sum += i

print sum





