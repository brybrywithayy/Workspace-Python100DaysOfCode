# Using the input() Function

input("What is your name?")     # prompts user to enter a string

# we can also do it this way (without using variables)
print("Hello " + input("What is your name?")) 

# input function runs first
# then print to console
# interestingly the program will substitute the user string in for the function
# this happens without assigning the value entered by the user to a variable

# can also do the traditional way
name = input("What is your name?")
print("Hello " + name)

# printing the number of characters in a string
print(len(input("What is your name?")))

# nested function calls go on the stack to execute in reverse order
# input() prompts user and passes string on
# len() works on the input string
# print() outputs the results of len()