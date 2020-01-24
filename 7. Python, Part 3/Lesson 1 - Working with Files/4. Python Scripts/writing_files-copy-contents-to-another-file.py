# Udacity > Intro to the Programming Nanodegree >
# Python part 3 > 1. Working with Files > Section 26:
# Writing output to a file

# writing files - copy the contents of a file to another file

# Copy contents of one file to another
with open("numbers.txt") as reader:
    with open("copy.txt", "w") as copy:
        copy.write(reader.read())
