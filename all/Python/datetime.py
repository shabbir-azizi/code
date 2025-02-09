from tkinter import *
import datetime  # Importing the datetime module

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')  # Corrected variable name
    am = time.strftime('%p')   # Corrected variable name and format for AM/PM
    date = time.strftime('%d')  # Corrected format for day of the month
    month = time.strftime('%m')
    year = time.strftime('%Y')  # Corrected format for full year
    day = time.strftime('%a')
    
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(200, date_time)  # Moved outside of lab_hr.config

clock = Tk()
clock.title('**** Digital Clock ****')
clock.geometry('1000x500')
clock.config(bg='dark gray')

lab_hr = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='gray', fg="black")
lab_hr.place(x=120, y=50, height=110, width=100)

lab_hr_txt = Label(clock, text="Hour", font=('times new roman', 20, "bold"),
               bg='gray', fg="black")
lab_hr_txt.place(x=120, y=190, height=40, width=100)

lab_min = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='gray', fg="black")
lab_min.place(x=340, y=50, height=110, width=100)

lab_min_txt = Label(clock, text="Min.", font=('times new roman', 20, "bold"),
               bg='gray', fg="black")
lab_min_txt.place(x=340, y=190, height=40, width=100)



lab_sec = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='gray', fg="black")
lab_sec.place(x=560, y=50, height=110, width=100)

lab_sec_txt = Label(clock, text="Sec", font=('times new roman', 20, "bold"),
               bg='gray', fg="black")
lab_sec_txt.place(x=560, y=190, height=40, width=100)

lab_am = Label(clock, text="00", font=('times new roman', 50, "bold"),
               bg='gray', fg="black")
lab_am.place(x=780, y=50, height=110, width=100)

lab_am_txt = Label(clock, text="Am/Pm", font=('times new roman', 20, "bold"),
               bg='gray', fg="black")
lab_am_txt.place(x=780, y=190, height=40, width=100)

# Date Labels
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
lab_mo_txt.place(x=340, y=410, height=40, width=100)

lab_year = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='gray', fg="black")
lab_year.place(x=560, y=270, height=110, width=150)

lab_year_txt = Label(clock, text="Year", font=('times new roman', 20, "bold"),
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
