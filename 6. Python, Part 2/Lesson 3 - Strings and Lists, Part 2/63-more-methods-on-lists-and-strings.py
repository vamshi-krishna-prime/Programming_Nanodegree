# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 15:
# More methods on strings

# some of the most implemented methods are discussed below:

print('box' in 'big box of trouble')
print(3 in [1, 2, 3, 4])
print([2, 3] in [1, 2, 3, 4])
print([2, 3] in [1, [2, 3], 3, 4])

print('evil' not in 'elvis lives')
print([2, 3] not in [1, 2, 3, 4])

print('abracadabra'.find('cad'))
print('abracadabra'.find('woolly mammoth'))

# count methods counts the non overlapping occurrences
print('badger badger badger mushroom'.count('bad'))
print('aaaa'.count('aa'))
print([1, 2, 1, 2, 3, 4, 1, 2].count(1))
print([1, 2, 1, 2, 3, 4, 1, 2].count([1, 2]))
