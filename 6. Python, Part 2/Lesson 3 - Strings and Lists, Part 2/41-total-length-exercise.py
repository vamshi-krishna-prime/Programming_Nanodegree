# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 1:
# Operations on lists

# Exercise: Total length
'''
Write a function total_length that takes a list of strings and
returns the sum of the lengths of all the strings in that list.
For instance —

>>> total_length(['Queen', 'rules'])   # two strings, five chars each
10
>>> total_length([])   # empty list
0
>>> total_length(['balloons'])   # one string, eight chars
8
>>> total_length(["", '', "", ''])   # four empty strings
0


Suppose that you have a list of strings, such as ['foo', 'bar']. If
you do len(['foo', 'bar']), you'll get 2 (because there are two items
in the list). But maybe what you're interested in is the total number
of characters in all the strings in the list. Something like this:

>>> total_length(['foo', 'bar'])
6
# There are six characters total (three in each string),.
'''

# Instructions:
'''
1. Define a function called 'total_length' that takes one parameter
(a list of strings)
2. Inside a function, create a variable to keep track of the total.
You ca start by assigning it a value of 0.
3. Loop over the items in the list, for each of them, add length to
the current total.
4. After the loop finishes, return the total.
'''

'''
def total_length(list):
    total = 0
    for item in list:
        total += len(item)
    return total


list = input("Enter a list of strings")
print(f'Total length: {total_length(list)}')

The above code is not correct because, the input fuction turns the input
into string. Which means even if you give the input a list of strings,
it will take it as a gaint single string and siplay unusual behaviour.

try to give the input the following list for more understanding
['345345', 'srtgg'], to the above code, not below.
'''


def total_length(list_of_strings):
    total = 0
    for string in list_of_strings:
        total = total + len(string)
    return total


print(total_length(['Queen', 'rules']))
print(total_length([]))
print(total_length(['balloons']))
print(total_length(["", '', "", '']))
print(total_length(['foo', 'bar']))
