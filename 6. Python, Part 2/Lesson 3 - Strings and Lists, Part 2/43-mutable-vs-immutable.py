# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 3:
# Mutable vs. immutable

'''
List are mutable (can be modified)
Strings are immutable (cannot be modified)
'''

# Exercise 1 - Mutable
print('\nExercise 1 - Mutable:\n')

breakfast = ['toast', 'bacon', 'eggs']
print(breakfast)
# ['toast', 'bacon', 'eggs']

print(breakfast[0])
# 'toast'

breakfast[0] = 'spam'
print(breakfast)
# ['spam', 'bacon', 'eggs']

breakfast[1] = 'spam'
print(breakfast)
# ['spam', 'spam', 'eggs']

breakfast[2] = 'spam'
print(breakfast)
# ['spam', 'spam', 'spam']


# Exercise 2 - immutable
print('\nExercise 2 - immutable:\n')

breakfast = 'waffles'
print(breakfast)
new_breakfast = breakfast + ' and strawberries'
print(new_breakfast)

print(breakfast)
breakfast = breakfast + ' and strawberries'
print(breakfast)
# but here the concatenated 'breakfast' is a new string.
