# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 8: Indexing

'''
write a function called start_K that checks whether a string starts
with the letter K.

If the string starts with K, the function should return True. If it
doesn't, the function should return False.

For example:
if you print out 'start_K("Kelly")', it should display 'True'
if you print out 'start_K("Abe")', it should display 'False'
'''

# Approach 1 - long version
print("\nApproach 1 - long version")


def start_K(s):
    if s[0] == "K":
        return True
    else:
        return False


print(start_K("Kelly"))
print(start_K("Abe"))


# Approach 2 - short version
print("\nApproach 2 - short version")


def start_L(s):
    return s[0] == "K"
    # As expression itself evaluates to 'True', it is returned


print(start_L("Kelly"))
print(start_L("Abe"))
