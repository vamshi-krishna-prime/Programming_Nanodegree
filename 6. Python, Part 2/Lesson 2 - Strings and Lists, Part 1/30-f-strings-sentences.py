# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 16: f-strings


# Here's something kind of fun we can do using f-strings:
'''
What's your name?

Abe

Hi, Abe! It's very nice to meet you.

What's your favorite color?

vermillion

Ah, vermillion, what a lovely color!
'''

# Using f- strings:

name = input("What's your name?\n\n")
print(f"\nHi, {name}! It's very nice to meet you.\n")
color = input("What's your favorite color?\n\n")
print(f"\nAh, {color}, what a lovely color!")
