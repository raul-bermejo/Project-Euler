# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:01:53 2021

@author: rbv

Problem 16:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""
import time

start = time.time()

def strSum(n):
    """
    Given an integer, it will find the sum of its digits by passing it as an
    integer.
    """
    result = 0
    for val in str(n):
        result += int(val)
    return result

n = 2**1000


print(f"The sum of the digits of 2^15 is: {strSum(n)}")

end = time.time()
print(f"The program took {end-start:.4e} to run.")


