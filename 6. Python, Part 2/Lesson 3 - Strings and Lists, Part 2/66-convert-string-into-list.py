# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 17:
# Find and replace (1/2)

# Convert a string into a list


# Approach 1 (without using split method)
def list_conversion(string):
    list = []
    for index in string:
        list.append(index)
    return list


string = input('Enter a string: ')
print(' Approach 1: without using split method:')
print('list converted:' + str(list_conversion(string)))

# Approach 2 using split method
# this can be used only when the string has a specific separator
print(' Approach 2: using split method:')
string1 = 'Going to the work'
string2 = 'mangos, stawberry, pears'
string3 = 'c-a-t'
# so string.split() will not work
print(string1.split(' '))
print(string2.split(','))
print(string3.split('-'))
