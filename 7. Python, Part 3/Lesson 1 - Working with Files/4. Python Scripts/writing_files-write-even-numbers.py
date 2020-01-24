# Udacity > Intro to the Programming Nanodegree >
# Python part 3 > 1. Working with Files > Section 26:
# Writing output to a file

# writing files - write even number below 30 to a new file

with open("numbers.txt", "w") as writer:
    # Write even numbers from 0 to 30
    for num in range(0, 31):
        if num % 2 == 0:
            writer.write(f"{num}\n")
