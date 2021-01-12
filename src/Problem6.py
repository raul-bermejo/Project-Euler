# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:39:40 2021

@author: rbv

Problem 6: 

The sum of the squares of the first ten natural numbers is 385,
The square of the sum of the first ten natural numbers is 3025.

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""
import time

start = time.time()

lst = [i for i in range(1,101)]
squares = [i**2 for i in range(1,101)]

squareSum = sum(lst)**2
sumSquares = sum(squares)


diff = abs(sumSquares - squareSum)

print(f"The difference is given by {sumSquares} - {squareSum} = {diff}")
end = time.time()
print(f"The program took {end-start:.4e} to run.")


