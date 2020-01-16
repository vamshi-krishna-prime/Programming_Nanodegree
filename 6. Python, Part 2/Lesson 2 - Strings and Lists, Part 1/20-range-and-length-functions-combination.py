# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 10:
# Length and indexing


'''
We just learned about indexing, and also about how to get the length
of a string using the len function. And previously, we used the
range function with for loops. You've used each of these things
separately, but it turns out that there are some things you can do by
using them together. Let's play around and see what we can get...

The following code are executed in the python terminal/interpreter
'''

>>> range(3)
range(0, 3)

>>> word = "yay"
>>> len(word)
3

>>> word = "yay"
>>> range(len(word))
range(0, 3)

>>> word = "yay"
>>> length = len(word)
>>> range(length)
range(0, 3)


'''
some of these bits of code seem to have the same result.
For example, 'range(3)' and 'range(length(word))' did the same thing.

At this moment, this might seem kind of pointless. Why would we ever
want to do range(length(word)) instead of range(3)?

When we just look at these pieces of code by themselves, there is
no reason for it. But we'll start putting these things together to
form more complex code later.
'''

>>> word = "yay"
>>> for n in range(len(word)):
...     print(n)
0
1
2

>>> word = "yay"
>>> length = len(word)
>>> for n in range(length):
...     print(n)
0
1
2

>>> word = "yay"
>>> length = len(word)
>>> for n in range(length):
...     print(word[n])
y
a
y

>>> word = "happy"
>>> for n in range(len(word)):
...    print(n, word[n])

>>> for e in range(len("foo")):
...    print(e)
# Loops over the index positions.

>>> for e in "foo":
...    print(e)
# Loops over the characters.

>>> word = "foo"
>>> for e in word:
...    print(e)
# Loops over the characters.

>>> word = "foo"
>>> for e in range(len(word)):
...    print(e)
# Loops over the index positions.


# See whether below 2 loops execute same output or not
>>> word = "yay"
>>> for n in range(len(word)):
...     print(word[n])

>>> word = "yay"
>>> for ch in word:
...     print(ch)
