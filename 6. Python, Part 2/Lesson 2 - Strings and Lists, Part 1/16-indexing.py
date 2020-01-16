# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 8: Indexing

'''
Indexing starts from '0', so the  index count is always one less than
actual length.
For example:
'''

print()
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
# print("Hello"[5]) will throw IndexError

word = 'greetings'
word[7]

print()
print('word: ' + word)
print('length of the word is :', len(word))
print('First letter is at: ' + word[0])
print('Last letter is at: ' + word[len(word) - 1])
print()

print()
colors = ['red', 'blue', 'orange']
print(colors[0])
print(colors[1])
print(colors[2])
print()
