# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 13:
# Finding substrings(3/4)

# Counting substrings
'''
Earlier you wrote the count_character function, which counts the
number of occurrences of a character in a string:

>>> count_character("papa pony and the parcel post problem", "p")
6

But it would be much more useful to be able to count substrings, not
just characters. Like this:

>>> count_substring('love, love, love, all you need is love', 'love')
4
'''


# Approach 1 - using 'for loop'
def count_substring1(string, target):
    total = 0
    index = 0
    for index in range(len(string)):
        if string[index: index + len(target)] == target:
            total += 1
        index += 1
    return total


# Approach 2 - using 'while loop'
def count_substring2(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index: index + len(target)] == target:
            total += 1
        index += 1
    return total


'''
count_substring('AAAA', 'AA')

How many times does 'AA' occur in 'AAAA'? There's one sense in
which the answer is 2, and another sense in which it's 3. It depends
on whether matches are allowed to overlap!

'''


# Approach 3 - more refined
def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index: index + len(target)] == target:
            total += 1
            index += len(target)   # <- This is the key line
        else:
            index += 1
    return total


print("# Approach 1 - using 'for loop'")
print(count_substring1('AAAA', 'AA'))
print(count_substring1("papa pony and the parcel post problem", "pa"))
print(count_substring1('love, love, love, all you need is love', 'love'))

print("# Approach 2 - using 'while loop'")
print(count_substring2('AAAA', 'AA'))
print(count_substring2("papa pony and the parcel post problem", "pa"))
print(count_substring2('love, love, love, all you need is love', 'love'))

print('Approach 3 - more refined')
print(count_substring('AAAA', 'AA'))
print(count_substring("papa pony and the parcel post problem", "pa"))
print(count_substring('love, love, love, all you need is love', 'love'))
