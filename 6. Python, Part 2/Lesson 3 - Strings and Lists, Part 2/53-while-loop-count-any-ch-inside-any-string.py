# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 8:
# While loops(4/5)

# Exercise - write a function to count 'o' in 'bonobos' using while loop:


# solution
def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total


# another approach
def count_character2(long, short):
    count = 0
    index = 0
    word = long
    while index < len(word):
        if word[index] == short:
            count += 1
        index += 1
    print(f'count: {count}')


print(f'count: {count_character("bonobos", "o")}')
print(f'count: {count_character("balloons", "o")}')
count_character2("abracadabra", "a")
count_character2("seashell", "s")
