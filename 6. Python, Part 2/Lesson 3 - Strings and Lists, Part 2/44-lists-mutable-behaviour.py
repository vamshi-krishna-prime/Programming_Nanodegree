# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 3:
# Mutable vs. immutable


# Lists - Mutable behaviour

print('\nLists - Mutable behaviour')
print('Before append: ')
list1 = [1, 2, 3]
list2 = list1
print(f'list1: {list1}')
print(f'list2: {list2}')

list2.append(4)
print('After appending list2: ')
print(f'list1: {list1}')
print(f'list2: {list2}')

# strings - immutable behaviour

print('\nstrings - immutable behaviour')
print('Before append: ')
string1 = 'abc'
string2 = string1
print(f'string1: {string1}')
print(f'string2: {string2}')

print('After appending string2: ')
string2 += 'd'
print(f'string1: {string1}')
print(f'string2: {string2}')


# Lists - Mutable behaviour
print('\nLists - Mutable behaviour')
print('Initial lists: ')
first_list = [1, 2, 3]
second_list = first_list
print(f'first list: {first_list}')
print(f'second list: {second_list}')

first_list.append(4)
print('After appending first_list with 4: ')
print(f'first list: {first_list}')
print(f'second list: {second_list}')

second_list.append(5)
print('After appending second_list with 5: ')
print(f'first list: {first_list}')
print(f'second list: {second_list}')

second_list[0] = "Woah!"
print('After modifying second_list: ')
print(f'first list: {first_list}')
print(f'second list: {second_list}')
