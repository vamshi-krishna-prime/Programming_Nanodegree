# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 10:
# Length and indexing


'''
We just learned about indexing, and also about how to get the length
of a string using the len function. And previously, we used the
range function with for loops. You've used each of these things
separately, but it turns out that there are some things you can do by
using them together. Let's play around and see what we can get...
'''

print()
word = "yay"
for n in range(len(word)):
    print(n)

print()
word = "yay"
length = len(word)
for n in range(length):
    print(n)

print()
word = "yay"
length = len(word)
for n in range(length):
    print(word[n])

print()
word = "happy"
for n in range(len(word)):
    print(n, word[n])

print()
# Loops over the index positions.
for e in range(len("foo")):
    print(e)

print()
# Loops over the characters.
for e in "foo":
    print(e)

print()
# Loops over the characters.
word = "foo"
for e in word:
    print(e)

print()
# Loops over the index positions.
word = "foo"
for e in range(len(word)):
    print(e)

print()
# See whether below 2 loops execute same output or not
word = "yay"
for n in range(len(word)):
    print(word[n])

print()
word = "yay"
for ch in word:
    print(ch)
