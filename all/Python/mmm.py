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