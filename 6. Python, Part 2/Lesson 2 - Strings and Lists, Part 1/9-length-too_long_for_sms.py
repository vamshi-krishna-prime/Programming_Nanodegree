# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 4: Length


# Too long for SMS

'''
SMS messages (and old-school Twitter posts) are limited to 140 characters.
In the workspace below (or in your own terminal, if you prefer), write a
function called too_long that tells whether a string is too long to be
sent in a single SMS message.

add some code to help test your function (with a short string and a
long string).
'''

# Approach 1
# ----------------


def too_long(s):
    length = len(s)
    if length > 140:
        return True
    else:
        return False


# ----------------
long_string = '''
SMS messages (and old-school Twitter posts) are limited to 140 characters.
In the workspace below (or in your own terminal, if you prefer), write a
function called too_long that tells whether a string is too long to be
sent in a single SMS message.

add some code to help test your function (with a short string and a
long string).
'''

short_string = 'short message'

# No neeed to use 'if too_long(long_string) == True:' because
# function itself returns 'True', which is enough to proceed True clause.
if too_long(long_string):
    print('Long string')
    print('Too long to be sent in a single SMS message')
else:
    print('Short string')
    print('string can be sent in a single SMS message')
# sometimes the return can be 'None' so use 'elif' condition further

if too_long(short_string):
    print('Long string')
    print('Too long to be sent in a single SMS message')
else:
    print('Short string')
    print('string can be sent in a single SMS message')


# --------------------------------------------

# Approach 2
# ----------------

def too_long(s):
    return len(s) > 140


# ----------------
'''
This one may not be as intuitive yet. Consider that len(s) > 140 is an
expression that will evaluate to either True or False. So this one line
of code does basically the same thing as the five lines you see in the
other version!
'''
