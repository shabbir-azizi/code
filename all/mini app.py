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
#900 + 200 =1100 

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





"""

syntax:

var_name {key:value, key2:value2}

"""






#step1 intitialize a dict
menu ={}#empty
#step2 how to add element

menu ["gulab jaman"] = 10
#step3 how to remove a element
del menu ["gulab jaman"]

#step4 how to access key 
menu["chicken rool"] = 240

# step5 hoe to update
menu["chicken rool"] = 300
"""price = menu["chicken rool"]
print(price)"""

 



price = menu["palak paneer"]
print(price)


# step6 hoe to clear a dictionary

# menu.clear()

# how to fine a lenght of a dictinory

print(menu)
print(len(menu))


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
