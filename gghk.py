# Python Basics

# 1. Print Statement
print("Hello, World!")

# 2. Variables and Data Types
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

# 3. Taking User Input
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

# 4. Conditional Statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 5. Loops
for i in range(5):  # Loop from 0 to 4
    print("Iteration:", i)

count = 0
while count < 3:
    print("Count:", count)
    count += 1

# 6. Functions
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))

# 7. Lists
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Orange")
print(fruits)

# 8. Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])

# 9. Exception Handling
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")

# 10. File Handling
with open("sample.txt", "w") as file:
    file.write("This is a sample file.")
print("Basic Python concepts covered!")


