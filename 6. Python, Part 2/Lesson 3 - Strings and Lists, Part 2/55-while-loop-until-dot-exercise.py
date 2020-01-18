# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 9:
# While loops(5/5)

# Exercise - Until Dot:
'''
Write a function called until_dot that takes a string argument and
returns the portion of that string before the first dot character.
(a.k.a., a period or full-stop). For example:

>>> until_dot("This is a sentence. This is another.")
'This is a sentence'
>>> until_dot("192.168.200.2")
'192'
If there are no dots in the string, return the whole string:

>>> until_dot("No dots here")
'No dots here'
'''

# Instructions:
'''
1. Before the loop, create a variable to keep track of the
current index position.
2. The while statement will need to check, if the current index
position is less than the length of the string.
3. And it will also need to check to make sure that the character
at the current position is not a dot.
4. Finally, the function should return a slice, from the start of
the string up to the index position of the first dot.
'''


# Here's one way to write the until_dot function using while loop:
def until_dot(s):
    index = 0
    while index < len(s) and s[index] != '.':
        # No dots yet, keep going.
        index += 1
    # We either found a dot or ran out of string.
    return s[:index]


# And here's another, using 'for' instead of 'while':
def until_dot2(s):
    for index in range(len(s)):
        if s[index] == '.':
            # A dot! Return everything up to here.
            return s[:index]
    # We ran out of string without seeing any dots.
    # Return the whole string.
    return s


print(until_dot("This is a sentence. This is another."))
print(until_dot("No dots here"))

print(until_dot2("192.168.200.2"))
print(until_dot2("No dots here"))

'''
Both of these are examples of a technique called linear search.
In a linear search, we start at the beginning of a sequence and look
at each item in the sequence until we find one that matches what
we're looking for. When we either find it, or run out of items, we stop.
'''
