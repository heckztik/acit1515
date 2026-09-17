## Creating variables and assigning values
# Create a variable named x and store an integer (whole number) inside it

x = 10

# Create a variable named y and store a string (any characters between single or double quotes) inside it

y = "string"

# Create a variable named z and store a float in it

z = 32451.421

## Changing values stored in variables
# Change the value stored in the x variable to a new string

x = "New String"

# Change the value stored in the y variable to a new boolean

y = True

# Change the value store in the z variable to a different float

z = 481.429

## Getting input from a user
# Print the value the user entered from the previous section

user_input = input("Input a value: ")
print(f"You entered: {user_input}")

# Print the (current) value of the variable x  

print(x)

# Print the *type* (not the value itself) of the value stored in the y variable

print(type(y))

## Concatenation (joining two strings together)
## Create two variables, one containing the string CIT, and another containing the string 1515

program = "CIT"
class_number = "1515"

# Using the two variables and a hard-coded letter, print the word ACIT1515 to the terminal

print(f"A{program}{class_number}")