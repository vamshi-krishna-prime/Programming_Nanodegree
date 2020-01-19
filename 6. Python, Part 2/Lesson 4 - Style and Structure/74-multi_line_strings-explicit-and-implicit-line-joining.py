# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 4. Style & Structure > Section 4:
# Multi-line strings (2/2)

# Explicit line-joining

story = "Once upon a time there was a very long string that was \
         over 100 characters long and could not all fit on the \
         screen at once."
print('\n' + story)


# Implicit line-joining
'''
There's also another type of line-joining that doesn't require the
backslash. In Python, any expressions inside parentheses ( ) ,
square brackets [ ], or curly braces { } can be split over more
than one line. For example, if we have a long list, we can do this:
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
           29, 30, 31, 32, 33, 34, 35, 36, 38, 29, 40, 41, 42]
print()
print(my_list)

story = ("Once upon a time there was a very long string that was "
         "over 100 characters long and could not all fit on the "
         "screen at once.")

print()
print("Once upon a time there was a very long string that was "
      "over 100 characters long and could not all fit on the "
      "screen at once.")

print()
print("foo" + "bar")
print()
print("foo" "bar")
