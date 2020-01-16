# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 9:
# The range function, revisited


'''
Earlier, we used the range function with for loops.
We saw that instead of using a list like this:
'''

print()
for side in [0, 1, 2, 3]:
    print(side)
print()

# Range can be used like below:
for n in range(4):
    print(n)
print()

'''
So we can pass range up to three arguments.
what the three range parameters do:

1. The first parameter is the number to start with.
2. The second parameter is the number to stop at (or rather, to
stop before, since it's excluded).
3. The third parameter is the step size (i.e., how large a step to
take when counting up).

Notice that start and step are optional—
if you leave either (or both) out, the function will just go with
the defaults— a start of 0 and a step of 1.

range(5) is same as range(0, 5, 1)
range(0, 5) is same as range(0, 5, 1)
range(4) is same as range(0, 4, 1)
range(0, 4, 1) is same as range(0, 4, 1)
range(2, 5) is same as range(2, 5, 1)
'''

print()
for n in range(5):
    print(n)

print()
for n in range(1, 4):
    print(n)

print()
for n in range(97, 101):
    print(n)

print()
for n in range(0, 10, 2):
    print(n)

print()
