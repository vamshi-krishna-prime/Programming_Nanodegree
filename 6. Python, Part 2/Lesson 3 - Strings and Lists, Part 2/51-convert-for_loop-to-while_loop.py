# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 7:
# While loops(3/5)

# Exercise - convert below 'for loops' into 'while loops':

word = "cat"

# for loop 1
print('for loop 1:')
for index in range(len(word)):
    print(index)

# for loop 2
print('for loop 2:')
for index in range(len(word)):
    print(word[index])


# while loop 1
index = 0
# As we used it earlier its current value is '2', reset it to '0'
print('while loop 1:')
while index < len(word):
    print(index)
    index += 1

# while loop 2
index = 0
# As we used it earlier its current value is '2', reset it to '0'
print('while loop 2:')
while index < len(word):
    print(word[index])
    index += 1
