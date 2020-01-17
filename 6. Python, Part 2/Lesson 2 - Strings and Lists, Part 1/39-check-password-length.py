# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 22:
# Boolean values

# Password length checker - Exercise
'''
Many web services want users to have passwords that are at least
eight characters long, but it can be a problem if passwords are
too long. Your goal will be to write a function that checks any
given string to see if it's a good length.
'''
# Instructions:
'''
1. Define a function 'good_length' with one parameter (for the string to check)
2. The function should return 'True' if the string is between 8 and 64
characters long, and 'False' otherwise.
'''


def good_length(s):
    # Return 'Flase' if password is not alphanumeric
    if not s.isalnum():
        return False
    # Return 'True' if password is between 8 and 64 characters long
    return len(s) > 8 and len(s) < 64


password = input("Enter the desired password: ")
print('Good Password:', good_length(password))
