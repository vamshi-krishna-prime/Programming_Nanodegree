# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 10:
# Infinite loops and breaking out


'''
A break statement will always skip to the end of the innermost 'while'
or 'for' loop. If you have a loop inside another loop, it will only
exit the inside loop.

The goal is to return the first multiple pair of 512.
Here's a piece of code that uses break incorrectly. This code is intended
to find values of x and y that, when multiplied together, give the number
512.
'''


def find_512_incorrect():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                break
                # does not do what we want!
    return f"{x} * {y} == 512"


def find_512_all():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                print(f"{x} * {y} == 512")
                break
    return f"{x} * {y} == 512"


def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                return f"{x} * {y} == 512"


print()
print('find_512_incorrect'.center(24, '*'))
print(find_512_incorrect().center(24))
# gives a false result of '99 * 99 == 512'

print()
print('find_512_all'.center(24, '*'))
print(find_512_all().center(24))
# returns all multiple
# only the return statement is centered but not print statements

print()
print('find_512'.center(24, '*'))
print(find_512().center(24))
# returns first multiple pair of 512
