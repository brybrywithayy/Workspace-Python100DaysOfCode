# No way to save the data that this function takes as written below
input("What is your name?")

# however, we can assign the data to a variable
name = input("What is your name?")
print(name)             # output is user-entered

# can reassign variable to another values
name = "Angela"
print(name)             # output is Angela

# using variables to refactor previous exercise
name = "Jack"                       # value assigned
print(name)

name = "Angela"                     # different value assigned
print(name)

name = input("What is your name?")  # user-entered value assigned
length = len(name)                  # assign the length of the string to variable

print(length)                       # print the length of the string by calling variable

# CODING EXERCISE - Variables
# Switch the values of a and b 
a = input("a:")
b = input("b:")

# my code:
temp = a
a = b
b = temp
# my code ends 

print(a)
print(b)

####################
# Naming Variables #
####################

# use variable names that make sense - should be self-explanatory
# Rules:
    # use meaningful names
    # if multi-word, use underscore
    # no numbers at the beginning
    # no spaces in variable names
