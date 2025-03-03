
# Output Frame
# Keyboard Frame
main_frame.grid() 
window.mainloop()



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




import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack()

geometry_string = "1150x950+500+25"
print(f"Setting geometry: {geometry_string}")
root.geometry(geometry_string)

root.mainloop()










