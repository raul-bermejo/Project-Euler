# -*- coding: utf-8 -*-
"""
@author: rbv

Problem 21:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time
import os

start = time.time()

def div_sum(n):
    "Returns the sum of all proper divisors up to n"
    sum = 0
    for j in range(1, n//2 + 1):
        if n % j == 0:
            sum += j
    return sum

result = 0
upper_bound = 10000

# Brute-force approach
for i in range(upper_bound):
    a = div_sum(i)
    if div_sum(a) == i and i != a:
            result += i
    

print(f"The  the sum of all the amicable numbers under 10000 is: {result}")
end = time.time()
print(f"The program took {end-start:.4e} to run.")
