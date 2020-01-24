# Udacity > Intro to the Programming Nanodegree >
# Python part 3 > 1. Working with Files > Section 16:
# The script footer

# Execute as 'python -u filename.py' for unbufferred/time delayed output

# Double-underscore ("dunder") variables
'''
the key point is:

If we directly run my_script.py, then __name__ gets set to '__main__'.
If we import my_script,py, then __name__ gets set to 'my_script'.
'''

print("I run all the time!")

if __name__ == '__main__':
    print("I've been run directly!")

if __name__ == 'my_script':
    print("I've been imported!")
