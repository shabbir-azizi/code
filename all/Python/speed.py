# from logging import root
# from pydoc import text
# import tkinter as tk
# root = tk.Tk()
# label1 = tk.Label(text='welcome to ss coder guy')
# label1.grid(row =0,column=0)
# text
# # relief
# # height
# # width
# # bd
# # bg
# # fg
# root.mainloop()
import tkinter as tk
window = tk.Tk()
window.title("Typo Speed Practise")
window.geometry("1150x950+500+25")
window.resizable(True,True)


# Main Frame
main_frame = tk.Frame(window,bg='white',bd=4)


# Title Frame
frame_title = tk.Frame(main_frame, bg='red', relief='flat')
lbl_title = tk.Label(frame_title, text='speed', font='Algerian 35 bold', bg='gray', fg='black', relief='groove', bd=10, width=30)
lbl_title.grid(row=0, column=0,pady=10)
frame_title.grid(row=0,column=0)


# Test Frame
selected_paragraph ='A paragraph is a series of sentences that are organized and coherent, and are all related to a single topic. Almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs.'
frame_test = tk.Frame(main_frame,bg='white',relife='flate')
# paragraph
lbl_paragraph = tk.Label(frame_test,text=selected_paragraph,wraplength=1000,justify='left')
lbl_paragraph.Grid(row=0,column=0)
# input box


frame_test.grid(row=0,column=0)


# Output Frame
# Keyboard Frame
main_frame.grid() 
window.mainloop()





















# 1. Hello, World!
print("Hello, World!")

# 2. Variables and Data Types
x = 5  # Integer
y = 3.14  # Float
name = "Alice"  # String
is_active = True  # Boolean
print(x, y, name, is_active)

# 3. Conditional Statements
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 4. Loops
# For loop
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# 5. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 6. Lists and Dictionaries
# List
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana

# Dictionary
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice

# 7. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create an object
alice = Person("Alice", 25)
alice.greet()

# 8. File Handling
# Write to a file
with open("example.txt", "w") as file:
    file.write("Hello, file!")

# Read from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 9. Exception Handling
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")

# 10. Importing Modules
import math
print(math.sqrt(16))  # Output: 4.0