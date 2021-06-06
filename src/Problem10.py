# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:45:02 2021
@author: rbv
"""
import time
import math

start = time.time()


def sumSievePrimes(N):
    """
    Finds any nth prime.
    
    Parameters:
    ----------
    N: int
       Upper threshold representing Nth prime
    
    Returns:
    -------
    primeSum:  int
               Sum of sequential N primes
    """
    
    lst = []
    lst.append(2)                                                               # initialize list with first prime
    
    num = 3
    while num < N:                                               # we don't need to check any other even number
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            lst.append(num)
        
        num += 2
    
    primeSum = sum(lst)
    return primeSum


N = 2000000
primeSum = sumSievePrimes(N)

print(f"The sum of primes up to 2 million is: {primeSum}.")

end = time.time()
print(f"The program took {end-start:.4e} to run.")