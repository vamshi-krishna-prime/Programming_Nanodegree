# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 16: f-strings


# Do it in the terminal:
'''
f-strings is something that was added to Python in version 3.6—
so in order for this to work on your own computer, you must be sure
to have Python 3.6 or later. As a reminder, you can check which version
you have by going to your terminal and entering:

python3 --version
'''
>>> import math
>>> import math
3.141592653589793
>>> f"pi is about {math.pi:.6}"
pi is about 3.14159
# This is because of ':.6' inside f-strings (formatted strings)

'''
Suppose that we want to get the following string:

'The aardwolf eats termites.'
'''

>>> animal = "aardwolf"
>>> food = "termites"
>>> "The " + animal + " eats " + food + "."
# Works

>>> animal = "aardwolf"
>>> food = "termites"
>>> "The {animal} eats {food}"
# Doesn't work.

>>> animal = "aardwolf"
>>> food = "termites"
>>> f"The " {animal} " eats " {food} "."
# Doesn't work.

>>> animal = "aardwolf"
>>> food = "termites"
>>> f"The {animal} eats {food}."
# Works
