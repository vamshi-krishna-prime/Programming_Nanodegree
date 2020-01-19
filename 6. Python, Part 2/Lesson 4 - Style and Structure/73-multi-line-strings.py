# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 4. Style & Structure > Section 3:
# Multi-line strings (1/2)

'''
Sometimes we end up wanting to use very long strings, and this can
cause some problems.
If you run pycodestyle on this, you'll get the following message:

some_script.py: E501 line too long

For such reasons, the Python style guide recommends keeping all
lines of code to a maximum of 79 characters in length—or even
72 characters, in some cases.
'''

'''
EOL stands for End Of Line. And a key thing to understand is that
this is actually a character in your code editor—it's just an
invisible one. In some code editors, there's an option to make these
visible.
'''

story = "Once upon a time there was a very long string that was \
         over 100 characters long and could not all fit on the \
         screen at once."
print('\n' + story)

# It prints, but there are a bunch of extra spaces between some of the words.


# One option would be to simply remove the indentation:

story = "Once upon a time there was a very long string that was \
over 100 characters long and could not all fit on the \
screen at once."
print('\n' + story)

# This would work, but it makes the code harder to read. We need a better
# solution.


# Instead of the escape character, how about if we use triple quotes?

story = """Once upon a time there was a very long string that was
           over 100 characters long and could not all fit on the
           screen at once."""
print('\n' + story)

# It prints the string, but there are a bunch of extra spaces between some
# of the words.


'''
What if we try using multiple strings, and using the + operator to
concatenate them? Like this:'

story =  "Once upon a time there was a very long string that was " +
         "over 100 characters long and could not all fit on the " +
         "screen at once."
print(story)

It throws the error Invalid syntax.
'''

# What if we try both concatenation and the escape character?

story = "Once upon a time there was a very long string that was " + \
        "over 100 characters long and could not all fit on the " + \
        "screen at once."
print('\n' + story)

# It prints the string perfectly.


# Here's something rather different:

story = ("Once upon a time there was a very long string that was "
         "over 100 characters long and could not all fit on the "
         "screen at once.")
print('\n' + story)

# It prints the string perfectly.

'''
This should be a bit surprising. Why would this work?

The reason is a combination of two lesser-known Python features:
Implicit line-joining and automatic string-literal concatenation.
'''
