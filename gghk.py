


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



               bg='gray', fg="black")
lab_year_txt.place(x=560, y=410, height=40, width=110)

lab_day = Label(clock, text="00", font=('times new roman', 35, "bold"),
               bg='gray', fg="black")
lab_day.place(x=780, y=270, height=110, width=100)

lab_day_txt = Label(clock, text="Day", font=('times new roman', 20, "bold"),
               bg='gray', fg="black")
lab_day_txt.place(x=780, y=410, height=40, width=100)

date_time()
clock.mainloop()

lab_date = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='gray', fg="black")
lab_date.place(x=120, y=270, height=110, width=100)

lab_date_txt = Label(clock, text="Date", font=('times new roman', 20, "bold"),
               bg='gray', fg="black")
lab_date_txt.place(x=120, y=410, height=40, width=100)

lab_mo = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='gray', fg="black")
lab_mo.place(x=340, y=270, height=110, width=100)

lab_mo_txt = Label(clock, text="Month.", font=('times new roman', 20, "bold"),
               bg='gray', fg="black")
