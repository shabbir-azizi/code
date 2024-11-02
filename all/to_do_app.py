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

        # if operation == 1:






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




import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "x" if current_player == "0" else "0"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "x"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()


import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "x" if current_player == "0" else "0"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "x"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
