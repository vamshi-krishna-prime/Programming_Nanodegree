# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 11:
# Finding substrings(1/4)

# Locating a substring
'''
When we search a string for substrings, we'll use index number
to describe where the substring is found. For instance, if we
search for 'ook' in 'cookbook', we'll say that it's found at
positions 1 and 5. This means that if we take a slice of length 3
starting from one of these positions, we'll see that substring:
'''
# find 'ook' inside 'cookbook'
string = 'cookbook'
print(f'string: {string}')
location = 5
size = 3
print(f'substring: {string[location: location+size]}')

# find the two 'in' s and 'asc' in 'fascinating' word.
word = "fascinating"

location = 4
size = 2
print(word[location: location + size])

location = 8
size = 2
print(word[location: location + size])

location = 1
size = 3
print(word[location: location + size])
