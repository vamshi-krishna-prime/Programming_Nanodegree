# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 6:
# While loops(2/5)

# Exercise:

'''
construct a word triangle using the string 'Tenochtitlan' and while loop
'''

s = "Tenochtitlan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])
