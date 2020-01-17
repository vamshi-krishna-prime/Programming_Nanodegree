# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 17:
# Strings to numbers to strings


# Below are some examples of code that we ran in the Python interactive interpreter.

>>> n = input("Please enter a number: ")
Please enter a number: 2
>>> n * 2
'22'

>>> n = input("Please enter a number: ")
Please enter a number: 2
>>> n + 2
TypeError

>>> n = input("Please enter a number: ")
Please enter a number: 2
>>> int(n) + 2
4

>>> n = int(input("Please enter a number: "))
Please enter a number: 2
>>> n + 2
4

'''
Suppose that we have a number stored in a variable:
>>> n = 7
And we want to generate a string like this:

'The lucky number is 7.'
'''

>>> n = 7
>>> 'The lucky number is ' + n + '.'
# Doesn't work

>>> f'The lucky number is {n}.'
# Works

>>> 'The lucky number is ' + str(n) + '.'
# Works
