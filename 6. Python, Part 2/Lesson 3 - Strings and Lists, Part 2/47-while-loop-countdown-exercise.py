# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 5:
# While loops(1/5)

# Countdown Exercise:
'''
In the workspace below, see if you can write a while loop that
prints a countdown, like this:

10
9
8
7
6
5
4
3
2
1
Blastoff!
'''

# Instructions:
'''
1. Before the loop create a new variable, say'n' to keep track
of the countdown.
2. write a 'while' statement that checks the current value of 'n'.
3. Inside the loop, print the current value of the 'n'.
4. Also inside the loop, update the value of 'n'. (otheriwse, it'll be
an infinite loop).
5. After the loop, add a statement to print 'Blastoff!'.
'''

# Time module
'''
The countdown isn't so great the way it is—the loop runs so fast that
it pretty much looks like the numbers just appear on the screen at the
same time. If we wanted to make it more like a real countdown, we would
need to have Python pause between printing each number.

We can do that by using a module called the time module.
'''

import time

print('\nCountdown Exercise:')
n = 10
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print("Blastoff!")
