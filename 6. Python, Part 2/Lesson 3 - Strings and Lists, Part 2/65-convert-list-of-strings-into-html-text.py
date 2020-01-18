# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 16:
# Joining

# Exercise: Line breaks

'''
Here is a list that contains some lines of poetry:

lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

To put these on a web page, we'd like to put an HTML <br> tag between
each two lines.

Write a function breakify that takes a list of strings, and returns a
single string with <br> inserted between each two strings in the list.
For instance, testing it on the above list should produce this result:

>>> breakify(lines)
'Haiku frogs in snow<br>A limerick came from Nantucket<br>Tetrametric
drum-beats thrumming, Hiawathianic rhythm.'
'''
# Soltuion:


def breakify(strings):
    return "<br>".join(strings)


lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

print(breakify(lines))
