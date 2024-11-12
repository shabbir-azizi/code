
# name = "Alice"
# # Integer
# age = 25
# # Float
# height = 5.9
# # Boolean
# is_student = True

# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Is a student:", is_student)
# a = 10
# b = 3
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)
# print("Exponent:", a ** b)
# number = 7

# if number > 0:
#     print("Positive number")
# elif number == 0:
#     print("Zero")
# else:
#     print("Negative number")
# # For loop
# for i in range(5):
#     print("For loop iteration:", i)

# # While loop
# count = 0
# while count < 5:
#     print("While loop iteration:", count)
#     count += 1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         return f"Hello, my name is {self.name} and I'm {self.age} years old."
    
# person1 = Person("Alice", 25)
# print(person1.greet())
# # Writing to a file
# with open("example.txt", "w") as file:
#     file.write("Hello, file handling in Python!")
# # Reading from a file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print("File content:", content)
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")  # Adding an item
# print("Fruits list:", fruits)
# print("First fruit:", fruits[0])  # Accessing an item

# definw the menu of resturant
menu={
    'pizza':900,
    'burger':200,
    'plater':3000,
    'chicken rool':250,
    'coffee':100,
    'drinks':150,
    'juise':210,
    'fruits':400,
}

# Greet
print("welcome to the ABC restaurant")
print(" pizza: RS 900\n burger: RS 200\n plater: RS 3000\n chicken rool: RS 250\n coffee: RS 100\n drinks: RS 150\n juise: RS 210\n fruits: RS 400")

order_total = 0
#900 = 200 =1100

item_1 = input("enter the name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1] #0 +50
    print(f"your item {item_1} has been added to your order")
else:
    print(" order item {item_1} is not available yet")
another_order =input("do you want to add another item?(YES/NO) ")
if another_order == "yes":
        item_2 = input("enter the name of second item =")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"your item{item_2}has been added to your order")
        else:
            print(f"orderd item {item_2} is not available yet!")

print(f"the total amount of items to pay is {order_total}")

        # another_order = input("do you want to add another item? (yes/no)")     
