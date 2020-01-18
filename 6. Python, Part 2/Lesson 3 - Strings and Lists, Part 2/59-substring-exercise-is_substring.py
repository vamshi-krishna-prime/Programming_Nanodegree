# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 12:
# Finding substrings(2/4)

# Writing an is_substring function
'''
Our first goal will be to write a function, is_substring, that simply
checks whether one string is a substring of another. If the first string
is a substring of the other, it should return True; otherwise, it should
return False. Like this:

>>> is_substring('oo', 'book')
True
>>> is_substring('pony', 'abracadabra')
False
>>> is_substring('dab', 'abracadabra')
True

This is very similar to the starts_with function we wrote earlier,
except that it will check the whole string—not just the beginning of it.
'''

# Instructions:
'''
1. Define the function so it accepts two parameters (substring and string)
2. Loop over the index position of the string.
3. At each position, check if the current slice is equal to the target
substring. If it is return 'True'.
4. If the loop finishes and the substring hasn't found, return 'False'.
'''


# Approach 1 - using 'for loop'
def is_substring1(substring, string):
    for index in range(len(string)):
        if string[index: index + len(substring)] == substring:
            return True
        index += 1
    return False


# Approach 2 - using 'while loop'
def is_substring2(substring, string):
    index = 0
    while index < len(string):
        if string[index: index + len(substring)] == substring:
            return True
        index += 1
    return False


print('is substring: ' + str(is_substring1('oo', 'book')))
print('is substring: ' + str(is_substring1('pony', 'abracadabra')))
print('is substring: ' + str(is_substring2('dab', 'abracadabra')))
print('is substring: ' + str(is_substring2('ff', 'waffles')))
