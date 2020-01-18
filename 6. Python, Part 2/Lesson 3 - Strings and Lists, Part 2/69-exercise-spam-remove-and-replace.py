# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 18:
# Find and replace (2/2)

# Exercise : Find and replace SPAM

'''
That prankster is back, and this time they've spammed my breakfast.
I was going to have:
'Scrambled eggs, bacon, and toast.'

But instead, now I have:
'Scrambled SPAM!s, bacon, and toast.'

In fact, they seem to have replaced all of the 'egg's with 'SPAM!'.
Instead of:
'Hot eggdrop soup, and curry with eggplant.'

We now have:
'Hot SPAM!drop soup, and curry with SPAM!plant.'

If we just run our 'remove_substring' function on these strings, that
won't really work:
'Hot drop soup, and curry with plant.'

We really do need our find-and-replace function now!
'''

# Instructions:
'''
1. Define a function replace_substring() with three parameters (one for
the main string, second for the substring and third for the string to
be replaced with).
2. When the target substring (to be removed) is located, append the
replacement string to the list in its place.
'''


def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replacement)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


spammed_string1 = 'Scrambled SPAM!s, bacon, and toast.'
spammed_string2 = 'Hot SPAM!drop soup, and curry with SPAM!plant.'
spammed_word = 'SPAM!'
replacement = 'egg'

print('Spammed string 1: ' + spammed_string1)
print('After spam removal: ' +
      str(replace_substring(spammed_string1, spammed_word, replacement)))
print('Spammed string 2: ' + spammed_string2)
print('After spam removal: ' +
      str(replace_substring(spammed_string2, spammed_word, replacement)))
