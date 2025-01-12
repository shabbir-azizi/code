from tkinter import *

clock = Tk()
clock.title('**** Digital Clock ****')
clock.geometry('1000x500')
clock.config(bg='yellow')

lab_hr = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='red', fg="white")
lab_hr.place(x=120, y=40, height=110, width=100)
lab_min = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='red', fg="white")
lab_min.place(x=340, y=40, height=110, width=100)
lab_sec = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='red', fg="white")
lab_sec.place(x=560, y=40, height=110, width=100)

lab_am = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='red', fg="white")
lab_am .place(x=780, y=40, height=110, width=100)

clock.mainloop()
