def task():
    tasks =[]#empty list
    print("----WELCOME TO THE TASK MANNAGEMENT APP----")

    total_task =int(input("Enter how many tast you want to add="))#5
    for i in range (1, total_task+1):
        task_name =input(f"enter task{i} = ")#enter task 3 =
        tasks.append(task_name)

    print(f"today's task are\n{tasks}")

    while True:
        operation = int(input("enter 1-add\nd-update\n3-delete\n4-view\n5-exit/stop/"))

    




# print("Hello, World!")
# a = 10
# b = 5
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# name = input("Enter your name: ")
# print("Hello, " + name)
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
# print(factorial(5))
# class Person:
#def __init__(self, name, age):
#self.name = name
#self.age = age
#     def greet(self):
#         return "Hello, " + self.name
#         person1 = Person("Alice", 25)
# print(person1.greet())
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# person1 = Person("Alice", 25)
# print(person1.greet())
# def greet(name):
#     return "Hello, " + name
# def fibonacci(n):
#     fib_seq = [0, 1]
#     for i in range(2, n):
#         fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
#     return fib_seq
# print(factorial(5))
# Writing to a file
# with open("example.txt", "w") as file:
#     file.write("Hello, this is a sample file.")

# # Reading from a file
# with open("example.txt", "r") as file:
# content = file.read()
#print(content)  # Output: Hello, this is a sample file.
