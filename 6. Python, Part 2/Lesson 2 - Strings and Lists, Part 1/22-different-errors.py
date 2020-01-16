# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 11: IndexError


'''
We just learned about indexing, and also about how to get the length
of a string using the len function. And previously, we used the
range function with for loops. You've used each of these things
separately, but it turns out that there are some things you can do by
using them together. Let's play around and see what we can get...

Try the following in the python interpreter
'''

>> 2 + "bears"
TypeError

>> print(donkey)
NameError

>> print(donkey)
SyntaxError

>> import explosion
ModuleNotFoundError

>> no_words = ""
>> print(no_words[0])
IndexError: string index out of range

>> word = "dog"
>> for n in range(10):
...    print(word[n])
IndexError: string index out of range
