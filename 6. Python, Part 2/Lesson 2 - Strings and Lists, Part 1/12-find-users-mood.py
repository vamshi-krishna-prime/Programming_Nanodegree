# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 5:
# Looping over things

'''
Complete the code so that it checks the message for exclamation marks '!'
(like above) and also question marks '?', and prints a different message
depending on which one it finds.

if there is an '?' in message print: "Sense much curiosity in you, I do."
if there is an '?' in message print: "Enthusiastic. you are."
'''

message = input("What do you have to say, hm?\n")

for ch in message:
    if ch == "?":
        print("Sense much curiosity in you, I do.")
    if ch == "!":
        print("Enthusiastic, you are.")
