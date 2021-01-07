# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:31:55 2021

@author: rbv

Problem 3: 
    
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time

start = time.time()

prime = 600851475143

def largest_prime_factor(n):
    """
    Finds the largest prime factor of any number
    
    Parameter:
    ---------
    n: int
       Number to be factorised
    
    Returns:
    -------
    largestPrimeFactor: int
                        Largest prime factor of input n.
    """
    factors = []
    d = 2
    while n > 1:                            # input should be larger than 1
        while n%d == 0:
            factors.append(d)               # append prime factor
            n/= d                           
        d += 1
    
    largestPrimeFactor = max(factors)
    return largestPrimeFactor
    
largestPrimeFactor = largest_prime_factor(prime)   

print(f"The largest prime factor of {prime} is {largestPrimeFactor}.")

end = time.time()
print(f"The program took {end-start:.4e} to find the largest prime factor.")

