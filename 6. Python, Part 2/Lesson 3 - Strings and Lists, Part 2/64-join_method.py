# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 16:
# Joining

# join method

words = ['my', 'dog', 'has', 'fleas']
print(' '.join(words))
print(''.join(words))
print(' silly '.join(words))

print('-'.join('cat'))

linker = ' and a '
print(linker.join(['apple', 'bunny', 'cracker']))

password = ['walrus', 'potato', 'gavel', 'explore']
print(''.join(password))

# ['this', 'is', 'wrong'].join(words) will generate AttributeError
print("['this', 'is', 'not', 'wrong']".join(words))
