include <iostream>

}
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


