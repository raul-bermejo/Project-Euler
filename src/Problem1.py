# -*- coding: utf-8 -*-
"""
Problem 1:
    
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

start = time.time()
# Create a list with all such multiples
lst = []

for i in range(1000):
    if (i%5==0 or i%3==0):
        lst.append(i)
    else:
        pass

# Now find the sum of that list
s = sum(lst)

print(lst)

end = time.time()

print(f"The sum of  all the multiples of 3 or 5 below 1000 is: {s}")
print(f"The program took {end-start:.4e} seconds.")
