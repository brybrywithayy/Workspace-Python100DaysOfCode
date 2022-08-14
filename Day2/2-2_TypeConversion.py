# Type Errors, Type Checking and Type Conversion

num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

######################
# Determining data type of a variable
print(type(num_char))       # class int

######################
# Type Conversion - Casting
new_num_char = str(num_char)   # converts variable to a string

print("Your name has " + new_num_char + " characters.")     # works as expected now

######################
# Example 2
a = 123

print(type(a))      # class int