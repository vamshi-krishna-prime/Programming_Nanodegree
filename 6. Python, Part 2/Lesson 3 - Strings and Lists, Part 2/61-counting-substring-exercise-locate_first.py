# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 14:
# Finding substrings(4/4)

# Counting substrings Exercise - locate First

'''
Let's start off with a version that just gives the location of the
first instance of the substring. We'll call it locate_first.

The function should find and return the first location of a substring.
But if the substring is not present, it should return -1 (you'll see
why we chose -1 soon).

>>> locate_first('ook', 'cookbook')
1
>>> locate_first('base', 'all your bass are belong to us')
-1
'''


def locate_first(sub, string):
    index = 0
    while index < len(string):
        if string[index: index + len(sub)] == sub:
            return index
        else:
            index += 1
    return -1


print(locate_first('ook', 'cookbook'))
print(locate_first('base', 'all your bass are belong to us'))
