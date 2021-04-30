# -*- coding: utf-8 -*-
"""
@author: rbv

Problem 22:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time


# In this problem, we cannot use textbook recursion as it is far too slow for
# large fibonacci numbers. We can use the matehmatical exponentiation, which gives
# the following formula: F(2k) = F(k)*[2*F(k+1)-F(k)] where k is int.
def fast_fibo(n):
    "Returns F(n), F(n+1) n by using mathematical exponentiation"
    if n == 0:
        return (0,1)
    else:
        a, b = fast_fibo(n//2)          # where (a,b) = (F(n//2), F(n//2 + 1))
        c = a*(2*b - a)
        d = b**2 + a**2
        if n%2 == 0:
            return (c, d)
        else:
            return (d, c+d)

start = time.time()

val = True
i = 1
while val:
    f_i, _ = fast_fibo(i)                                               # calculate the i_th fibonacci number
    # Calculate the num of digits by turning
    # into string and getting length, then have
    # statement for the length
    n_digits = len(str(f_i))                   
    if n_digits >= 1000:
        val = False
        break
    # Increment index
    i += 1

# test, _ = fast_fibo(4782) 
# print(len(str(test)))
# print(n_digits)
print(f"The index of the first term in the Fibonacci sequence to contain 1000 digits is {i}")
end = time.time()
print(f"The program took {end-start:.4e} seconds to run.")
