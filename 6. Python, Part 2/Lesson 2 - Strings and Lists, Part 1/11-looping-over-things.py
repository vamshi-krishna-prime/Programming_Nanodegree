# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 5:
# Looping over things

print('--------')
for thing in ["some", "list", "of", "things"]:
    print(thing)

print('--------')
for thing in "Hello!":
    print(thing)

print('--------')
for ch in "Hello !":
    print(ch)

print('--------')
'''
This ability to loop over the characters in a string is very handy.
For example, if we combine this with an if test, we can check all of
the letters in a string—and have a certain block of code only run when
a particular character is detected.
'''

for ch in "Hello!":
    print(ch)
    if ch == "!":
        print("I'm excited too!!!")
