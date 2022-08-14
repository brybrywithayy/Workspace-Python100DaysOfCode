# Coding Exercise
# evaluate a number and determine if it is even or odd

# starter code
number = int(input("Which number do you want to check? "))
# end starter code

remainder = number % 2

if remainder == 0:
  print("This is an even number")
else:
  print("This is an odd number")
  
# can also write:
"""
if number % 2 == 0:
  print("This is even")
else:
  print("this is odd")
"""
