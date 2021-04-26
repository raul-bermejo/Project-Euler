# -*- coding: utf-8 -*-
"""
@author: rbv

Problem 22:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import time
import os

start = time.time()

# Define function to give alphabetical value of a name
def alphabetical_value(s):
    # This function inputs a roman string and finds the numerical
    # value of the string using ascii value
    val = 0
    for char in s:
        # Ensure that the character is within [A,Z] by checking ASCII value
        if (ord(char) >= ord("A") and ord(char) <= ord("Z")):
            ascii_val = ord(char) - (ord("A") - 1)                          # Standarize so "A" has a value of 1
            val += ascii_val
    return val

# Define path to data file
path_to_folder = r"C:\Users\rbv\OneDrive\Escritorio\Side__Projects\Project_Euler\Project-Euler\data"
file_name = r"p022_names.txt"
abs_path = os.path.join(path_to_folder, file_name)


# Extract data in file
file = open(abs_path, 'r')
names = file.readlines()[0].split(",")                                  # file is read like a list with only one element
file.close()

# Sort names list
names = sorted(names)

# Iterate through sorted list to calculate sum of scores
result = 0
for i, char in enumerate(names):
    # Calculate ith_score
    pos = i+1
    alph_val = alphabetical_value(char)
    ith_score = pos*alph_val

    result += ith_score

print(f"The total of all the name scores in the file is {result}")
end = time.time()
print(f"The program took {end-start:.4e} to run.")
