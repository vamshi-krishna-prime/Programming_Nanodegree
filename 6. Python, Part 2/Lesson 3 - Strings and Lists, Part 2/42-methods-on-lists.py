# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 2:
# Methods on lists

'''
Append method:
Adds its argument as a single item to the end of the list. It only
ever adds one item to a list.

Extend method:
Treats its argument as a sequence and adds each item in the sequence
to the end of the list. In other words, it adds a sequence of items
to a list.
'''

# we'll explore several different list methods.
print('\n**First Exercise**\n')
words = ["echidna", "dingo", "crocodile", "bunyip"]
print("Original list".ljust(16) + ': ' + str(words))

words.append("platypus")
# The word "platypus" has been added to the end of the list, after "bunyip".
print("After append".ljust(16) + ': ' + str(words))

words.extend("abc")
# Three strings, 'a', 'b', and 'c', are now at the end of words.
print("After extend".ljust(16) + ': ' + str(words))

words.extend(["kangaroo", "wallaby"])
# The list words now has the words 'kangaroo' and 'wallaby' added to the end.
print("After extend".ljust(16) + ': ' + str(words))

words.reverse()
# After running this, the first item in words is 'wallaby'.
print("After reverse".ljust(16) + ': ' + str(words))

words.sort()
'''
It changes words so that it's sorted in alphabetical order, starting
with 'a' and ending with 'wallaby'.
'''
print("After sort".ljust(16) + ': ' + str(words))
print()


# Second Exercise
print('\n**Second Exercise**\n')
my_list = [1, 2, 3]
print(f'orignal list: {my_list}')

my_list.append([4, 5, 6])
print(f'after append: {my_list}')
# [1, 2, 3, [4, 5, 6]]

my_list.extend([4, 5, 6])
print(f'after extend: {my_list}')
# [1, 2, 3, 4, 5, 6]

my_list.append("abc")
print(f'after append: {my_list}')
# [1, 2, 3, 'abc']

my_list.extend("abc")
print(f'after extend: {my_list}')
# [1, 2, 3, 'a', 'b', 'c']


# Third Exercise
print('\n**Third Exercise**\n')
first_list = [1, 2, 3]
second_list = [4, 5, 6]
third_list = [1, 2, 3]

print('First List'.ljust(15) + ': ' + str(first_list))
print('Second List'.ljust(15) + ': ' + str(second_list))

for item in second_list:
    first_list.append(item)

print('Resulting List'.ljust(15) + ': ' + str(first_list))
