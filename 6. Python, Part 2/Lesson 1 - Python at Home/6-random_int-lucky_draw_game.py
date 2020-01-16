# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 1. Python at Home > Section 14

from random import randint

# Function to generates a random number everytime it executes


def generator():
    return randint(1, 10)


# Function takes user input and returns 'True' or 'False'
# depending whether the user wins the lucky draw!
def rand_guess():
    # calls generator() which returns a
    # random integer between 1 and 10
    random_number = generator()

    # defining the number of
    # guesses the user gets
    guess_left = 3

    # Setting a flag variable to check
    # the win-condition for user
    flag = 0

    # looping the number of times
    # the user gets chances
    while guess_left > 0:

        # Taking a input from the user
        guess = int(input("Pick your number to "
                          "enter the lucky draw\n"))

        # checking whether user's guess
        # matches the generated win-condition
        if guess == random_number:

            # setting flag as 1 if user guessses
            # correctly and then loop is broken
            flag = 1
            break

        else:

            # If user's choice doesn't match
            # win-condition then it is printed
            print("Wrong Guess!!")

        # Decrementing number of
        # guesses left by 1
        guess_left -= 1

    # If win-condition is satisfied then,
    # the function rand_guess returns True
    if flag is 1:
        return True

    # Else the function returns False
    else:
        return False


if rand_guess() is True:
    print("Congrats!! You Win.")
else:
    print("Sorry, You Lost!")
