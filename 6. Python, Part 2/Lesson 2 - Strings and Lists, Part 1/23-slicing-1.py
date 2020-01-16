# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 12: Slicing(1/2)

'''
string[first_value : second_value]

1. indexing starts woth '0'
2. first_value is inclusive
3. second_value is exclusive
'''

print()
word = 'apple'
print(word[0:3])
print(word[:3])
print(word[1:3])
# Below will not produce IndexErrror, explanation at bottom
print(word[:12])
print("balloon"[:3])
print("balloon"[3:])

print()
print("slice the word"[0:5])
print("slice the word"[:5] + ' ' + "slice the word"[10:])

print()
print("python"[0:2])
print("python"[1:5])
print("python"[0:5])
# Below will not produce IndexErrror, explanation at bottom
print("python"[0:6])
print("python"[:])

print()
print("udacity"[3:])
print("new york city"[:3])
print("battle of yorktown"[10:14])
print("downtown newark"[4:8])

print()
word = "definitely"
length = len(word)
print(word[:length])
print(word[:length - 2])
print(word[length - 8:])
print(word[length - 8:length - 2])


# No Index Errors with slice operations
'''
Slice operations never cause IndexError. A slice that tries to
extract characters off of the end of the string, will instead just
return as much as it can get, even if that's nothing at all —
'''

print()
print('Extracting out of bounds/index')
extracted_word = "presto"[1024:4096]
print('extracted word = ' + "presto"[1024:4096])
print('extracted word length = ' + str(len(extracted_word)))
