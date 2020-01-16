# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 1. Python at Home > Section 10: Functions revisited

# Approach 1
print("\nApproach 1")


def say_hello():
    return "Hello1!"


say_hello()
# No output is printed as 'print function' is not used anywhere


# Approach 2
print("\nApproach 2")


def say_hello2():
    return "Hello2!"


print(say_hello2())
# Output of "Hello2!" will be displayed


# Approach 3
print("\nApproach 3")


def say_hello3():
    print("Hello3!")


say_hello3()
# Output of "Hello3!" will be displayed as print is used inside function


# Condition 1
print("\nCondition 1")
greeting1 = say_hello()
# No output is displayed as we just assigned the function to a variable but
# not made any print statements
greeting2 = say_hello2()
# No output is displayed as we just assigned the function to a variable but
# not made any print statements
greeting3 = say_hello3()
# Output is displayed as print function is associated with the
# 'function called' (say_hello3), but nothing is assigned to the
# 'greetings3' variable

# Condition 2
print("\nCondition 2")
print(greeting1)
# Output of 'Hello1!'will be displayed
print(greeting2)
# Output of 'Hello2!'will be displayed
print(greeting3)
# Output of 'None' will be displayed as no value is assigned to the
# 'greetings3' variable.

# Approach 4
print("\nApproach 4")


def greeting():
    return "Hello!"
    return "Goodbye!"


print(say_hello())
# Only the first return will be displayed

# Approach 5
print("\nApproach 5")


def confuse():
    print("bears")
    return 42


confuse()
print("\n")
print(confuse())
print("\n")
print(confuse() * 2)
print("\n")
unknown = confuse()
print("\n")
print(unknown)


# Approach 6
print("\nApproach 6")


def more_confused():
    2 + 2


more_confused()
# nothing happens as neither 'return function' nor 'print' are defined
print(more_confused())
# displays "None" as nothing is returned from the function to print
