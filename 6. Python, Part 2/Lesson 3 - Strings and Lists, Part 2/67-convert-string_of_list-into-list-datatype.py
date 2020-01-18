# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 17:
# Find and replace (1/2)

# Convert a list in string form to a proper list

# A string representation of a list
string_list = "[1, 2, 3, 4, 5]"

# printing the string of list and its datatype
print("list in string datatype: " + "'" + string_list + "'")
print(type(string_list))

# Converting string to list
converted_list = string_list.strip('][').split(', ')

# printing the converted list and its datatype
print("converted list: ", converted_list)
print(type(converted_list))
