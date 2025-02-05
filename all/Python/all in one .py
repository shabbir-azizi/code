from tkinter import Tk, Button, Label, messagebox

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = Tk()
root.title("Tic-Tac-Toe")

buttons = [Button(root, text="", font=("Arial", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"
winner = False
label = Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()







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
