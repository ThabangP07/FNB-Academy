#String

# This code prints a simple message to the console

message = "Hello, World!"
print(message)

# Index a string elements
print(message[0])
print(message[1])
print(message[-1])

#Built-in Functions and methods
print(len(message))  # Length of the string 

print(message.upper())  # Convert to uppercase
print(message.lower())  # Convert to lowercase
print(message.split())  # Split the string into a list of words

#numerical values

num = 3
print(type(num))  # Check the type of num

num2 = 3.14
print(type(num2))  # Check the type of num2

# Variables

#valid variable names
my_variable = "Hello"
myVariable = "World"    
user = "Logan"

#invalid variable names
#1myVariable = "Hello"  # Cannot start with a number
#user-name = "Logan"  # Cannot contain hyphens
#user name = "Logan"  # Cannot contain spaces

#Arithmetic Operators

x = 10
y = 5       

print(x + y)  # Addition
print(x - y)  # Subtraction     
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y)  # Exponentiation

#operators on strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Concatenation
print(str1 * 3)  # Repetition

#Control flow - if/elif/else
num = 10

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else: 
    print("Negative number")