# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 14: Concatenation(1/2)


# Exercise: Adverbly
'''
In English, you can often form an adverb (such as quickly) by starting
with an adjective (like quick) and adding "ly" to the end.

(In Silicon Valley, you can often form a startup name by taking a noun
or verb and adding "ly" to the end.)

Write a function called adverbly that takes a string as input and returns
that string with "ly" appended to it.
'''


def adverbly(s):
    return s + 'ly'


verb = input('Enter a verb: ')
print(adverbly(verb))
