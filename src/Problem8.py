# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 08:12:56 2021

@author: rbv

Problem 8:
    
The four adjacent digits in the 1000-digit number that have the greatest 
product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the 
greatest product. What is the value of this product?
"""

import time
import re

start = time.time()

def stringProd(s):
    """
    Finds the product of an input str made of single-digit integers.
    
    Parameters:
    ----------
    s: str
       Contains single digit integers to be multiplied
    
    Returns:
    -------
    p: int
          Product of these elements
    """
    
    s = re.sub(r"\s", "", s)    # Remove all whitespace
    s = re.sub(r"\D.*", "", s)  # Remove everything starting at a non-digit
    
    p = 1
    lst = [int(s[i]) for i in range(len(s))]
    for num in lst:
        p *= num

    return p

def find_adjacent_GP(s, n):
    """
    Finds the n adjacent digits in an str input number s.t. they have the 
    greatest product.
    
    Parameters:
    ----------
    s: str
       Large digit
    n: int
       Number of adjacent digits
    
    Returns:
    -------
    GP: int
        Greatest product of all possible adjacent products
    """
    
    # Initialize variables
    size = len(s)
    start, end = 0, n
    currProd = 0
    prodLst = []
    
    # Loop over the input string to compute the product of 13 adjacents
    while (end < size-1):
        newProd = stringProd(s[start:end])
        if newProd > currProd:
            prodLst.append((newProd, start, end))
        # Increase counters
        start += 1; end += 1
        
    # Then find the maximum 
    
    return prodLst
    

largeNum = """73167176531330624919225119674426574742355349194934 
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""


N = 13                                                      # # of digits stated in the problem
lst = find_adjacent_GP(largeNum, N)
print(max(lst))

end = time.time()
print(f"The program took {end-start:.4e} to run.")


