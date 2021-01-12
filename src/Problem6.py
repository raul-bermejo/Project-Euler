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

# We can formalize the problem since they are finite summation of simple series
def sum_iSquares(n):
    """
    Find the sum of squares of sequential integers up to n starting from 1.
    
    Parameters:
    ----------
    n: int
       upper term
    
    Returns:
    -------
    s: int
       Sum of n squares
    """
    
    s = (n*(n+1)*(2*n + 1))/6
    return int(s)

def sum_i(n):
    """
    Returns the sum of sequential integers up to n starting from 1.
    
    Parameters:
    ----------
    n: int
       upper term
    
    Returns:
    -------
    s: int
       Sum of n squares    
    """
    
    s = (n*(n+1))/2
    return int(s)

n = 100

squareSum = sum_i(n)**2
sumSquares = sum_iSquares(n)


diff = abs(sumSquares - squareSum)

print(f"The difference is given by {sumSquares} - {squareSum} = {diff}")
end = time.time()
print(f"The program took {end-start:.4e} to run.")


