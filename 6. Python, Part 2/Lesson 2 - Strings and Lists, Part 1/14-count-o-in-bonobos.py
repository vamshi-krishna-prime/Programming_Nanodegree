# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 6:
# Counting things (1\2)

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
why does this line 'count = 0' have to go before the loop, rather
than inside the loop?
Go ahead and try putting it inside:
'''

for ch in "bonobos":
    count = 0
    if ch == "o":
        count = count + 1
print(count)

'''
result will be '0'

So why does this happen?
It's because the line count = 0 gets run every time the loop runs.
So count keeps getting reset back to 0 over and over, rather than counting
up like we want it to.

That is why we have to set the initial value of the count variable before
the loop. This is a common pattern that you will see in code, so keep it
in mind!
'''
