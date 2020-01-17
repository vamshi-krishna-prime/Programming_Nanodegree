# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 21:
# Methods on strings

# Check whether the string is a HTML element or not using string methods


def possible_tag(word):
    if word.startswith("<") and word.endswith(">"):
        print(word, "could maybe be an HTML tag")
    else:
        print(word, "is definitely not an HTML tag (but might contain "
              "one inside)")


element = input('Enter the string: ')
possible_tag(element)
