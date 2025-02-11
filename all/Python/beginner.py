a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("First number is the largest:", a)
elif b >= c:
    print("Second number is the largest:", b)
else:
    print("Third number is the largest:", c)



first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Sum =", first + second)


side = float(input("Enter square side length: "))
print("Area =", side**2)


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Average =", (a + b) / 2)



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Is first number greater or equal to second?", a >= b)




a = 4309565
b = 56467763
c = 86575456

print("Sum:", a + b + c)
print("Product:", a * b * c)
print("Subtraction result:", a - b * c)
print("Modulo result:", a % b * c)
