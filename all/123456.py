# String
name = "Alice"
# Integer
age = 25
# Float
height = 5.9
# Boolean
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is a student:", is_student)



a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)





number = 7

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")




# For loop
for i in range(5):
    print("For loop iteration:", i)

# While loop
count = 0
while count < 5:
    print("While loop iteration:", count)
    count += 1




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

person1 = Person("Alice", 25)
print(person1.greet())



# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, file handling in Python!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an item
print("Fruits list:", fruits)
print("First fruit:", fruits[0])  # Accessing an item

