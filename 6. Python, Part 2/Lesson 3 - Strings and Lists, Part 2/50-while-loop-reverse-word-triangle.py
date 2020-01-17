# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 6:
# While loops(2/5)

# Exercise:

'''
construct a word triangle using the string 'Abracadabra' and while loop
'''
# Approach 1 using increment
print('\nApproach 1 using increment:')
word = 'Abracadabra'
index = 0
while index < len(word):
    print(word[0:len(word)-index])
    index += 1


# Approach 2 using decrement
print('\nApproach 2 using decrement:')
s = "abracadabra"
index = len(s)
while index > 0:
    print(s[:index])
    index -= 1
