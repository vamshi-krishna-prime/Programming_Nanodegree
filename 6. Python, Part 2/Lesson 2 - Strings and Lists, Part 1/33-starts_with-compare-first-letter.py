# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 18:
# starts_with (1/3)

# Just comparing the first letter
'''
Our first goal will be as follows:
Create a function called 'starts_with' that takes two strings, and
indicates whether the first characters of those strings match. In
other words, it would do something like this:

>>> starts_with("apple", "art")
True
>>> starts_with("apple", "cart")
False
'''

# Instructions:
'''
1. Define a function 'starts_with' with 2 parameters(for the 2 strings).
2. Compare the first characters of the string.
3. If the characters are the same, return True, otherwise return False.
4. Remove the comments from the print statements ans run the script.
'''


def starts_with(s1, s2):
    if s1[0] == s2[0]:
        return True
    else:
        return False


print(starts_with("apple", "art"))
print(starts_with("apple", "cart"))

'''
But in programming, there's almost always more than one way to
do the same thing...
Here are some other attempts at the above solution:
'''


def starts_with2(s1, s2):
    if s1[0] != s2[0]:
        return False
    else:
        return True


# shortest approach
def starts_with3(s1, s2):
    return s1[0] == s2[0]


print(starts_with2("balloon", "cars"))
print(starts_with3("strawberry", "snakes"))
