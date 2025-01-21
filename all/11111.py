paragraph=("")


import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack()

root.mainloop()


print("Before creating the label")
my_label = tk.Label(root, text="Hello", font=("Arial", 20))
print("Label created successfully")


my_label = tk.Label(root, text="Hello", bg="red", font=("Arial", 20))  # Correct font format


frame = tk.Frame(root)
my_label = tk.Label(frame, text="Hello")



my_label = tk.Label(root, text="Hello", font=("Arial", 20))  # Valid font si


geometry_string = "1150x950+500+25"  # Corrected format
print(f"Setting geometry: {geometry_string}")
root.geometry(geometry_string)



import tkinter as tk

root = tk.Tk()
root.geometry("1150x950+500+25")  # Correct format: width x height + x_offset + y_offset
root.mainloop()



"<width>x<height>+<x_offset>+<y_offset>"


root.geometry("1150x950+500+25")  # Correct format




from tkinter import messagebox

def check_winner():
    for combo in[[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]:
        if buttons[combo[o]]["text"]== buttons[combo[1]]["text"]==buttons(combo[2])["text"] !="":
            buttons[combo[0]].config(bg ="green")
            buttons[combo[1]].config(bg ="green")
            buttons[combo[2]].config(bg ="green")
            messagebox.showinfo ("Tic-Tac-Toe", f"player {buttons[combo[0]]['text']} wins!")
            root.quit()


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()


def toggle_player():
    global current_player
    current_player ="x" if current_player == "0" else "0"
    label.config(text=f"player{current_player}'s turn")
root = tk.Tk()
root.title("Tic-Tac-Toe")
 

buttons = [tk.button(root,text ="",font=("normal", 25),width=6,height=2,command=lamda i=i: button_click(i))for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)
current_player ="x"
winner = False
labal = tk.labal (root, trxt= f"player{current_player}'s turn, font",font=("normal", 16))
labal.grid()





a = int(input("enter frist number"))

b = int(input("enter second number"))

c = int(input("enter third number"))

if(a >= b and a>= c ):
    print ("frist number is largest",a)

elif(b >= c):
    print("second number is largest",b)

else:
    print("third number is largest",c)

frist = int(input("enter frist : " ))
second = int (input("enter second :"))

print("sum =", frist + second )

side = float(input("enter square side :"))
print("area =", side**2)

a = float(input("enter frist :"))
b = float(input("enter second :"))
print("avg =",(a+b)/2)

a = int(input("enter second :"))

b = int(input("enter second :"))

print(a>=b)
from tkinter import messagebox

def check_winner():
    for combo in[[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]:
        if buttons[combo[o]]["text"]== buttons[combo[1]]["text"]==buttons(combo[2])["text"] !="":
            buttons[combo[0]].config(bg ="green")
            buttons[combo[1]].config(bg ="green")
            buttons[combo[2]].config(bg ="green")
            messagebox.showinfo ("Tic-Tac-Toe", f"player {buttons[combo[0]]['text']} wins!")
            root.quit()


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()


def toggle_player():
    global current_player
    current_player ="x" if current_player == "0" else "0"
    label.config(text=f"player{current_player}'s turn")
root = tk.Tk()
root.title("Tic-Tac-Toe")
 

buttons = [tk.button(root,text ="",font=("normal", 25),width=6,height=2,command=lamda i=i: button_click(i))for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)
current_player ="x"
winner = False
labal = tk.labal (root, trxt= f"player{current_player}'s turn, font",font=("normal", 16))
labal.grid()





a = int(input("enter frist number"))

b = int(input("enter second number"))

c = int(input("enter third number"))

if(a >= b and a>= c ):
    print ("frist number is largest",a)

elif(b >= c):
    print("second number is largest",b)

else:
    print("third number is largest",c)

frist = int(input("enter frist : " ))
second = int (input("enter second :"))

print("sum =", frist + second )

side = float(input("enter square side :"))
print("area =", side**2)

a = float(input("enter frist :"))
b = float(input("enter second :"))
print("avg =",(a+b)/2)

a = int(input("enter second :"))

b = int(input("enter second :"))

print(a>=b)





a=4309565
b=56467763
c=86575456
a+b+c
print(a+b+c)
print(a*b*c)
print(a-b*c)
print(a%b*c)
