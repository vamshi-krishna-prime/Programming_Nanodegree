# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 12: Slicing(1/2)

'''
Exercise: Word triangle

find a partially completed for loop.
Goal is to finish the loop so that it prints out the following:
d
de
def
defi
defin
defini
definit
definite
definitel
definitely
'''

# Approach 1
print('\nApproach 1:\n')

word = "definitely"
length = len(word)

for n in range(length):
    print(word[0:n + 1])


# Approach 2
print('\nApproach 2:\n')

new_word = ''
for ch in 'definitely':
    new_word += ch
    print(new_word)


'''
Each time through the loop, n gets larger. So [0:n] is a slice expression
that will start from the beginning of the string (at the character with
index 0) and go up until the character at index n. Since n is growing,
the string that gets printed will also grow longer each time.

Notice that we have to add + 1, because n starts at 0 and goes up to 9
(but we want it to start at 1 and go up to 10).
'''
