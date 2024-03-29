# -*- coding: utf-8 -*-
"""
Created on Thu March 17 08:51:07 2021

@author: rbv

Problem 13:
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import time
import math
from collections import Counter
from itertools import product

def triangularSequence(n):
    return sum([i for i in range(1,n+1)])

def find_primeFactors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n

def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def find_numDivisors(n):
    # Find prime factors and create prime count dictionary
    divisors = []
    pf = find_primeFactors(n)
    pf_countDict = Counter(pf)

    # For each prime factor, work out all the generated numbers
    # and store in a list of lists
    primePowers = [ [factor ** i for i in range(count + 1)]
                        for factor, count in pf_countDict.items() ]
    # To find the divisors, compute Cartesian product and find product 
    # of each pair
    for cartProd in product(*primePowers):
        divisors.append(prod(cartProd))

    return len(divisors)
    
start = time.time()
b = True
n = 30
while b is True:
    # Compute triangular number and check if div condition is met
    t = triangularSequence(n)
    nDivisors = find_numDivisors(t)
    if nDivisors > 500:
        b = False
        break
    n += 1
end = time.time()

print(f"First triangle number to have over 500 divisors is: {t}")
print(f"The code took {end-start:.2f}s to execute")


