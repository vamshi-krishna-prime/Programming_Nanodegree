# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 17:
# Find and replace (1/2)

# Exercise : Find and remove SPAM

'''
We're now ready to try our hand at finding and removing substrings
that we don't want. And good thing, too—someone has taken my beautiful
string...

'Hello world!'
...and spammed it!

'SPAM!HelloSPAM! worldSPAM!!'`
'''

# Instructions:
'''
1. Define the 'remove_substring' function with two parameters (for the
main string and the substring to be removed).
2. Create an empty lists to hold the output.
3. Loop pver the index numbers of the string.
4. Check if the substring at the current position is the target substring.
If it is, jump the index to skip over it.
5. Otherwise, append the current character to the output list and
advance the index by 1.
6. Finally, join the parts of the list back together to form a new
string and return it.
'''


def remove_substring(string, substring):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


spammed_string = 'SPAM!HelloSPAM! worldSPAM!!'
spamm_word = 'SPAM!'
print('Spammed string: ' + spammed_string)
print('After spam removal: ' + remove_substring(spammed_string, spamm_word))
