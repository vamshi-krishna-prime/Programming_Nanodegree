# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 2. Strings & Lists Part 1 > Section 3:
# More complex strings

# print the following lines as it is separetely
'''
To quote my favorite author, "let's go on an adventure!"
-----------------
"Is it very long?" Alice asked, for she had heard a good deal of
poetry that day.
"It's long," said the Knight, "but it's very, very beautiful."
'''


print("----")
print("This message\nis on two lines!")
print("----")
print("""This message
      is on two lines!, but with space""")
print("----")
print("""This message
is on two lines!""")
print("----")
print("This message"
      " is not on two lines!")
print("----")
print('To quote my favorite author, "let\'s go on an adventure!"')
print("----")
print("\"Is it very long?\" Alice asked, for she had heard a good"
      " deal of poetry that day.")
print("----")
print("\"It's long,\" said the Knight, \"but it's very, very beautiful.\"")
print("----Approach 1----")
# using line breaks
print('"Is it very long?" Alice asked, for she had heard a good deal '
      'of poetry that day.\n\n"It\'s long," said the Knight, "but it\'s '
      'very, very beautiful."')
print("----Approach 2----")
# using triple quotes
print("""
"Is it very long?" Alice asked, for she had heard a good deal of poetry that day.

"It's long," said the Knight, "but it's very, very beautiful."
""")


'''
But running the same code as shown below will result in syntax error
because the pyhton sees the first 3 quotes as start of the string and the
next 3 quotes that appear first as the ending quotes. But we can observe
that there are 4 quotes ending the string, leaving the last quote
unrecognizable, hence syntax error.
--------
print(""""Is it very long?" Alice asked, for she had heard a good deal of poetry that day.

"It's long," said the Knight, "but it's very, very beautiful."""")
--------
'''
