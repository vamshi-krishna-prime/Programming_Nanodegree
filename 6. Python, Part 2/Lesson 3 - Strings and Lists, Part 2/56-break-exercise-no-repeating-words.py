# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 10:
# Infinite loops and breaking out

# Exercise - Repeated words:

'''
Write an function to store the words input by the user
and exit the while loop when a word is repeated.

There's another way to exit from an infinite loop. Inside a while or
for loop, you can use the break statement to immediately exit the loop .
'''


def no_repeating():
    words = []
    while True:
        word = input("Tell me a word: ")
        if word in words:
            print("You told me that word already!")
            break
        words.append(word)
    return words


print(no_repeating())
