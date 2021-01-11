# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:24:43 2021

@author: rbv

Problem 4:
    
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time

start = time.time()

palindromes = []
thd = 999                                                                       # maximum number to check
for i in reversed(range(thd)):
    for j in reversed(range(thd)):                                              # loop reversly from 9999
        prod = i*j
        if (str(prod)[::-1] == str(prod)):
            palindromes.append((prod, i, j))                                    # store numbers and product as a tuple
            break

pali, num1, num2 = max(palindromes)
print(f"The largest 3 digit palindrome is given by {num1} x {num2} = {pali}")
   
end = time.time()
print(f"The program took {end-start:.4e} to run.")


