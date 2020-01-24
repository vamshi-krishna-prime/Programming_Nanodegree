# Udacity > Intro to the Programming Nanodegree >
# Python part 3 > 1. Working with Files > Section 19:
# Planning the solution to the profanity filter problem

# Execute as 'python -u filename.py' for unbufferred/time delayed output

# Create a string with 99 a's and one b.
# There will always be one b, but it will be at a random position
# from 0 to 99.

import random

letters = ['a'] * 100
b = random.randint(0, 99)
letters[b] = 'b'
letters = "".join(letters)

# Search for the letter b in the string.
# How many times will this print "Not yet" ?

print("Looking for 'b' ...")
pos = 0
while letters[pos] != 'b':
    pos += 1
    print("Not yet")
print("Found it!")
