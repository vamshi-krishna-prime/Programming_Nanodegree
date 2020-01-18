# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 14:
# Finding substrings(4/4)

# Counting substrings Exercise - locate_all

'''
Make a function that locates all instance of a substring.

The function should find and return the count of all substring occurrences.
But if the substring is not present, it should return -1 (you'll see
why we chose -1 soon).

>>> locate_all('cookbook', 'ook')
[1, 5]
>>> locate_all('yesyesyes', 'yes')
[0, 3, 6]
>>> locate_all('the upside down', 'barb')
[]
'''


def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index: index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches


print(locate_all('cookbook', 'ook'))
print(locate_all('yesyesyes', 'yes'))
print(locate_all('the upside down', 'barb'))
