# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 6:
# Counting things (2\2)

'''
counts the number of times 'o' appears in the string "bonobos".

steps to follow:
1. set the initial value of the 'count' variable to '0'
2. 'if' the current characteris an 'o', increase 'count' by '1'.
3. Finally, 'print' the final value of 'count'
'''

count = 0

for ch in "bonobos":
    if ch == "o":
        count = count + 1

print(count)


'''
Our code from the last script works fine, but it's not very
flexible—currently, it only checks for the letter o in a specific
string ("bonobos"). If we wanted to check other characters and other
strings, we would have to re-write the code each time.

Instead, it would be good to modify it so that we can give it any
character and any string.


Steps to follow:
1. Add a def statement for a function called 'count_character'
2. Add parameters for the string to be searched, and the character to count
3. Use these parameters in the body of the function, in place of the
hard coded strings that are currently there.
4. Test your function with the provided 'print' statements (You can add
 your own statements too.)
'''


def count_character(string, target):
    count = 0
    for ch in string:
        if ch == target:
            count = count + 1
    return count


print(count_character('bonobos', 'b'))
# count_character(bonobos, b) will not work as the arguments are not strings
print(count_character('Hello world', ' '))
print(count_character('Hello world', 'l'))
print(count_character('Hello world !!', '!'))
