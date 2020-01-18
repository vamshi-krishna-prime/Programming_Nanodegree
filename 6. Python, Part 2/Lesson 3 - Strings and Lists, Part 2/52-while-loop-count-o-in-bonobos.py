# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 8:
# While loops(4/5)

# Exercise - count 'o' in 'bonobos' using while loop:

count = 0
index = 0
word = 'bonobos'
while index < len(word):
    if word[index] == 'o':
        count += 1
    index += 1
print(f'count: {count}')
