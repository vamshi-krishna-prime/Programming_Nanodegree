# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 20:
# starts_with (3/3)

# Comparing whether long string starts with short string
'''
Write a function called starts_with that takes two strings as arguments,
—a long string and a short string and returns True if the first string
starts with the second string, and False otherwise.

In other words, we want a function that does this:

>>> starts_with("apple", "app")
True
>>> starts_with("banana", "ban")
True
>>> starts_with("manatee", "mango")
False
'''
# Instructions:
'''
In programming, there's almost always more than one way to do
something. Here's an alternative approach to the 'starts_with' function
that's quite different: Instead of using a for loop and checking each
pair of characters, we can simply use string slicing.

1. Define a function with 2 parameters 'long' and 'short'.
2. Use the slice operator [:] with the 'len' function to get the first
part of the long string.
3. If that slice matches the short string, return True. Otherwise return False.
'''


def starts_with_v1(long, short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True


def starts_with_v2(long, short):
    length = len(short)
    beginning = long[0:length]
    if beginning == short:
        return True
    else:
        return False


def starts_with_v3(long, short):
    return long[0:len(short)] == short


print(starts_with_v1("apple", "app"))
print(starts_with_v2("manatee", "mango"))
print(starts_with_v2("banana", "ban"))

# try the below code and see what happens (long and short are switched)
'''
starts_with_v1("tin", "tinkerbell")
starts_with_v2("tin", "tinkerbell")
starts_with_v3("tin", "tinkerbell")

The first one produces an IndexError, while the others just return False.
As version 2 and 3 use slicing operator there won't be IndexError.
'''
