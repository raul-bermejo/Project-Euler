# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 8:34:09 2021

@author: rbv

Problem 15:
Find the number of lattice paths form (0,0) to (20,20) in a 20x20 grid
"""
import time

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def BinomCoeff(n,k):
    nCk = factorial(n)/(factorial(n-k)*factorial(k))
    return int(nCk)
start = time.time()
# For lattice paths without restrictions, the number of paths is given
# by 2n choose n where n is the size of the grid
sizeGrid = 20
nPaths = BinomCoeff(2*sizeGrid, sizeGrid)
print(f"The number of lattice paths in a 20x20 grid is: {nPaths}")
end = time.time()
print(f"The program took {end-start:.4e} to run.")
