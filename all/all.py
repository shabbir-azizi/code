"""
"world"
'world'
"""

# creat a string
name = "shabbir"


# how to concatenate
""""sername = "azizi" 
print(name,""+sername)"""


def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero!"
    else:
        return "Invalid operation!"
        print(calculator(10, 5, "add"))


def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci(10))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(17))
print(is_prime(18))


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print(generate_password(12))


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)


a=32
b=43
a+b
print(a+b)


# to day 20,11,2024


# List manipulation example

# Create a list
numbers = [5, 2, 9, 1, 7, 6]

# Print the original list
print("Original List:", numbers)

# Sort the list in ascending order
numbers.sort()
print("Sorted List (Ascending):", numbers)

# Sort the list in descending order
numbers.sort(reverse=True)
print("Sorted List (Descending):", numbers)

# Reverse the list
numbers.reverse()
print("Reversed List:", numbers)

# Add an element to the list
numbers.append(10)
print("List after adding an element:", numbers)

# Remove an element from the list
numbers.remove(9)  # Removes the first occurrence of 9
print("List after removing an element:", numbers)

# Replace an element at a specific index
numbers[2] = 15
print("List after replacing an element:", numbers)

# Slice the list
sliced_list = numbers[1:4]  # Get elements from index 1 to 3
print("Sliced List (index 1 to 3):", sliced_list)

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
            if operation ==1:
                 add = input("enter task you want to add = ")
                 task.append(add)
                 print(f"task {add} has been successfull added...")
            elif operation == 2:
                 updated_val = input ("enter the task name you want to update =")
                 if updated_val in tasks:
                      up = input("enter new task =")
                      ind = task.index(updated_val)#2
                      tasks [ind]=up
                      print(f"updated task {up}")
            elif operation == 3:
                 del_val =input("which task you want to delete")
                 if del_val in tasks:
                      ind = tasks.index (del_val)
                      del tasks[ind]
                      print(f"task{del_val} has been deleted...")
            elif operation ==4:
                 print(f"total tasks = {tasks}")

            elif operation == 5:
                 print("closing the program....")
                 break
            
            else: 
                 print("invalid input")
