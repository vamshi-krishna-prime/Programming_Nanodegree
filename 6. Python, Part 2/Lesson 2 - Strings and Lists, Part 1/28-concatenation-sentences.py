# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 15: Concatenation(2/2)


# Here's something kind of fun we can do using concatenation:
'''
What's your name?

Abe

Hi, Abe! It's very nice to meet you.

What's your favorite color?

vermillion

Ah, vermillion, what a lovely color!
'''
# instructions:
'''
The code for this uses the input function to get strings from the user,
like their name and favorite color. It then uses the concatenation operator
to construct some responses based on what the user entered.

Steps to follow:
1. use the input function to get a response from the user, and assign
the response to a variable.
2. concatenate the user's response with another string, and print the result.
3. If you like, you can use '\n' in your strings to create blank lines.
'''
# solution:

name = input("What's your name?\n\n")
print("\nHi, " + name + "! It's very nice to meet you.\n")
color = input("What's your favorite color?\n\n")
print("\nAh, " + color + ", what a lovely color!")
