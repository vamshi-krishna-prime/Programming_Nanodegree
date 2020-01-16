# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 13: Slicing(2/2)

'''
Exercise: Abracadabra

The magic word abracadabra comes from an ancient superstition in
which people would write the word in a triangular pattern, dropping
one letter on each line, from "abracadabra" all the way down to "a".
The idea was, that as the word disappeared, so too would bad luck
disappear —

Today, we don't need magical inscriptions to make our strings vanish
away to nothing — we can do it using for loops and slices!

Write a function word_triangle that takes a string as its argument,
and prints out a triangle similar to the one above. You don't have
to center it, though. Here's an example of what it should look like:

>>> word_triangle("kitten")
kitten
kitte
kitt
kit
ki
k

This is very similar to the exercise you just did, but with some
important differences:

1. We start with the full word, and remove letters from the end.
2. We're making it into a function so that it can be called with
different words.
'''

# Solution:
'''
Here's one way to write the word_triangle function in the exercise above:


def word_triangle(word):
    length = len(word)
    for n in range(length):
        print(word[:length - n])


The slice expression here is word[:length - n]. Since length stays
the same while n grows, this means that on each pass through the loop,
length - n gets smaller and smaller, from length down to 1. And that
means that on each pass, the string that gets printed will be a shorter
and shorter piece of word.

There are a lot of other ways to write this, too!
'''


# 2 approaches (same in a sense)


def word_triangle(word):
    length = len(word)
    for n in range(length):
        print(word[:length - n])


def word_triangle2(string):
    for ch in range(len(word)):
        print(word[0:len(word)-ch])


word = input('\nEnter a word: ')
print('\nReverse word triangle:')
word_triangle(word)
print()
print('\nReverse word triangle:')
word_triangle2(word)
