def greet(name):
    """Function to greet a person with their name."""
    print(f"Hello, {name}!")
    
greet("Alice")  # Example usage of the greet function

def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b

result = add_numbers(5, 10)  # Example usage of the add_numbers function
print(f"The sum is: {result}")

def factorial(n):
    """Function to calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result_factorial = factorial(5)  # Example usage of the factorial function
print(f"The factorial of 5 is: {result_factorial}")
    
def greeting(name, message = "Hello"):
    """Function to greet a person with a custom message."""
    print(f"{message}, {name}!")

greeting("Mary")