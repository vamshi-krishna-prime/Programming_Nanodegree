# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 4:
# Augmented assignments


# Try them on interpreter

>>> n = 1
>>> n = n + 2

>>> n = 2
>>> n = n * 3
>>> n
6

>>> n = 5
>>> n = n / 2
>>> n
2.5

>>> n = 10
>>> n = n - 6
>>> n
4

>>> s = "Hello"
>>> s = s + " world!"
>>> s
'Hello world!'

'''
The effect of n = n + 1 and n += 1 is the same. The latter is called
an augmented assignment statement, because it's an assignment statement
but it augments the existing value rather than replacing it.

balloon = 5
balioon += 10   # causes NameError
because balloon is misspelled, this can be avoided using
augmented assignments
'''

>>> n = 2
>>> n *= 3
>>> n
6

>>> n = 5
>>> n /= 2
>>> n
2.5

>>> n = 10
>>> n -= 6
>>> n
4

>>> s = "Hello"
>>> s += " world!"
>>> s
'Hello world!'

>>> dog = "woof"
>>> dog *= 2
'woofwoof'

'''
balloon = 'abc'
balioon += 1     # will cause TypeError
'''
