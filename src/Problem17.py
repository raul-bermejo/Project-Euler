# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 08:22:11 2021

@author: rbv

Problem 17:

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
 words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The 
use of "and" when writing out numbers is in compliance with British usage.
"""
import time

start = time.time()

# Create a dictionary that maps numbers to strings
numDict = {n:0 for n in range(0,1001)}
# Initialize important values manually
numDict[0] = ''
numDict[1] = 'one'
numDict[2] = 'two'
numDict[3] = 'three'
numDict[4] = 'four'
numDict[5] = 'five'
numDict[6] = 'six'
numDict[7] = 'seven'
numDict[8] = 'eight'
numDict[9] = 'nine'
numDict[10] = 'ten'
numDict[11] = 'eleven'
numDict[12] = 'twelve'
numDict[13] = 'thirteen'
numDict[14] = 'fourteen'
numDict[15] = 'fifteen'
numDict[16] = 'sixteen'
numDict[17] = 'seventeen'
numDict[18] = 'eighteen'
numDict[19] = 'nineteen'
numDict[20] = 'twenty'
numDict[30] = 'thirty'
numDict[40] = 'forty'
numDict[50] = 'fifty'
numDict[60] = 'sixty'
numDict[70] = 'seventy'
numDict[80] = 'eighty'
numDict[90] = 'ninety'
numDict[1000] = 'one thousand'

# Now add 21-99
for i in range(21,101):
    if i%10 != 0:
        rightNum = int(str(i)[-1])
        leftNum = i//10
        numDict[i] = numDict[leftNum*10]+"-"+numDict[rightNum]

# Add the 100-900 in steps of 100
for i in range(100,901,100):
    leftNum = i//100
    numDict[i] = numDict[leftNum] + " hundred"

# Add the gaps between 101-999
for i in range(101,1001):
    if i%10 != 0:
        leftNum = i//100
        rightNum = int(str(i)[1:])
        numDict[i] = numDict[leftNum*100] + " and " + numDict[rightNum]

def stringCount(s):
    "This function counts roman characters in input string"
    

end = time.time()
print(f"The program took {end-start:.4e} to run.")


