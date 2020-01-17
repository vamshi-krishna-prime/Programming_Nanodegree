# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 19:
# starts_with (2/3)

# Comparing whether long string starts with short string
'''
Write a function called starts_with that takes two strings as arguments,
—a long string and a short string and returns True if the first string
starts with the second string, and False otherwise.

In other words, we want a function that does this:

>>> starts_with("apple", "app")
True
>>> starts_with("banana", "ban")
True
>>> starts_with("manatee", "mango")
False
'''

# Instructions:
'''
1. Define a function 'starts_with' with 2 parameters, 'long' and 'short'.
2. Create a 'for' loop that loops over the index numbers of the 'short' string.
3. For each index number compare the characters at the position.
4. As soon as there's a pair that does not match, return False.
5. If the looop finishes (all characters match), return True.
'''


def starts_with(long, short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True


print(starts_with("apple", "app"))
print(starts_with("manatee", "mango"))
print(starts_with("banana", "ban"))
