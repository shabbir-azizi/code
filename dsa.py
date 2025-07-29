lab_year_txt.place(x=560, y=410, height=40, width=110)

lab_day = Label(clock, text="00", font=('times new roman', 35, "bold"),
               bg='gray', fg="black")
lab_day.place(x=780, y=270, height=110, width=100)

lab_day_txt = Label(clock, text="Day", font=('times new roman', 20, "bold"),
               bg='gray', fg="black")
lab_day_txt.place(x=780, y=410, height=40, width=100)

date_time()
clock.mainloop()

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


