# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 4: Length

import unicodedata

'''
Python strings aren't just limited to characters that appear on an
English-language keyboard. Characters from other languages and writing
systems can appear in Python strings. So can special symbols such as emoji:
'''

print("Snakes! 🐍🐍🐍")

'''
There is a Python module called unicodedata that lets you look up
characters by name, including emoji:
'''
# see at the top of the script that we have imported unicodedata library
# try this in python interpreter
'''
>>> import unicodedata
>>> unicodedata.lookup("snake")
'🐍'
>>> unicodedata.lookup("cat")
'🐈'

'''

'''
Emoji are usually wider on screen than letters or numbers; in a
monospaced font they usually take up the space of two characters. They
also take up more computer memory. But the length of a Python string
depends only on the number of characters in it, not on what kind of
characters they are:
'''
# try this in python interpreter
'''
>>> len("🐍")
1
>>> len("🐍🐍🐍")
3
>>> len("蛇 = 🐍")
5
'''
