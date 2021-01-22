# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 08:51:07 2021

@author: rbv

Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
import math

start = time.time()

# To find the number of primes up to 1001
def sieve_primes(nth):
    """
    Finds any nth prime.
    
    Parameters:
    ----------
    nth: int
       Upper threshold representing nth prime
    
    Returns:
    -------
    nth_prime: int
               nth prime
    """
    
    lst = []
    lst.append(2)                                                               # initialize list with first prime
    
    num = 3
    
    while len(lst) < nth:                                               # we don't need to check any other even number
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            lst.append(num)
            
        num += 2
        
    nth_prime = lst[-1]
    
    return nth_prime

n = 10001
prime_10001th = sieve_primes(n)

print(f"The 10001th prime corresponds to {prime_10001th}") 
end = time.time()
print(f"The program took {end-start:.4e} to run.")


