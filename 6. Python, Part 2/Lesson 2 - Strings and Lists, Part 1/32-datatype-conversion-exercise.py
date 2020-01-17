# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 17:
# Strings to numbers to strings

# Exercise
'''
In this next exercise, your goal is to write a program that asks
the user for three numbers, adds those numbers up, and then prints
a message saying what the sum is. Like this:

Enter a number: 2
Enter another number: 1
Enter a third number: 3
2 + 1 + 3 = 6
'''
# Instructions:
'''
1. Use input to get the numbers and assign them to variables (call the
variables 'n1', 'n2', and 'n3')
2. Use 'int()' to convert the response to integers and then sum them up.
3. Print out the final message. Use f-strings to put it all together.
'''

n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
n3 = input("Enter a third number: ")
sum = int(n1) + int(n2) + int(n3)
# Approach 1 using f-strings
print(f"{n1} + {n2} + {n3} = {sum}")
# Approach 2 but clumsy
print(n1 + ' + ' + n2 + ' + ' + n3 + ' = ' + str(sum))
