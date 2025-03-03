  # 1. Basic Python Syntax
print("Welcome to the Python Guide!")  # Output a string

# Variables and Data Types
integer_var = 42
float_var = 3.14
string_var = "Python is fun!"
boolean_var = True

# List, Tuple, Set, and Dictionary
sample_list = [1, 2, 3, 4, 5]
sample_tuple = (10, 20, 30)
sample_set = {1, 2, 2, 3}  # Duplicate values are removed
sample_dict = {"name": "Alice", "age": 25}

# 2. Control Flow
# if-elif-else statement
if integer_var > 50:
    print("Greater than 50")
elif integer_var == 42:
    print("Equal to 42")
else:
    print("Less than 50")

# Loops
# For loop
for num in sample_list:
    print(f"Number: {num}")

# While loop
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1

# 3. Functions
def greet(name):
    """Function to greet a user"""
    return f"Hello, {name}!"

print(greet("Bob"))

# 4. File Handling
file_path = "example.txt"

# Writing to a file
with open(file_path, "w") as file:
    file.write("This is an example file.\nPython is great!")

# Reading from a file
with open(file_path, "r") as file:
    content = file.read()
    print(content)

# 5. Error Handling
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always executes.")

# 6. Classes and Objects
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} says hello!"

dog = Animal("Buddy", "Dog")
print(dog.speak())

# 7. Python Libraries
import math
import random
import datetime

# Math operations
print(f"Square root of 16: {math.sqrt(16)}")



