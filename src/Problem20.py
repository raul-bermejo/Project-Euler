# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:18:27 2021

@author: rbv

Problem 20:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import time

start = time.time()

# Define factorial
def factorial(n):
    """
    Finds the factorial i.e. n! of input integer n
    """
    lst = [i for i in range(1,n+1)]
    prod = 1
    for val in lst:
        prod *= val
    return prod

# Define a function to find the sum of the digits of input number
def strSum(n):
    """
    Given an integer, it will find the sum of its digits by passing it as an
    integer.
    """
    result = 0
    for val in str(n):
        result += int(val)
    return result

num = 100
digitSum = strSum(factorial(num))
print(f"The sum of digits in 100! is: {digitSum}")

end = time.time()
print(f"The program took {end-start:.4e} to run.")


