# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 9:
# While loops(5/5)

# Exercise - Mind the gap:
'''
write a while loop to print the string until it finds a space/gap.
For example, for input 'Mind the gap!', the output should be 'Mind'
'''

index = 0
s = "Mind the gap!"
while index < len(s) and s[index] != " ":
    index += 1
print(s[:index])
