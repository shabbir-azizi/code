from tkinter import *
def date_time():
    time =datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    Sec = time.strftime('%S')
    Am = time.strftime('%P')
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,date_time)






clock = Tk()
clock.title('**** Digital Clock ****')
clock.geometry('1000x500')
clock.config(bg='yellow')

lab_hr = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='red', fg="white")
lab_hr.place(x=120, y=50, height=110, width=100)

lab_hr_txt = Label(clock, text="Hour", font=('times new roman', 20, "bold"),
               bg='red', fg="white")
lab_hr_txt.place(x=120, y=190, height=40, width=100)

lab_min = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='red', fg="white")
lab_min.place(x=340, y=50, height=110, width=100)

lab_min_txt = Label(clock, text="Min.", font=('times new roman', 20, "bold"),
               bg='red', fg="white")
lab_min_txt.place(x=340, y=190, height=40, width=100)


lab_sec = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='red', fg="white")
lab_sec.place(x=560, y=50, height=110, width=100)


lab_sec_txt = Label(clock, text="Sec", font=('times new roman', 20, "bold"),
               bg='red', fg="white")
lab_sec_txt.place(x=560, y=190, height=40, width=100)

lab_am = Label(clock, text="00", font=('times new roman', 60, "bold"),
               bg='red', fg="white")
lab_am .place(x=780, y=50, height=110, width=100)


lab_am_txt = Label(clock, text="Am/Pm", font=('times new roman', 20, "bold"),
               bg='red', fg="white")
lab_am_txt.place(x=780, y=190, height=40, width=100)


date_time()
clock.mainloop()


















import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article titles (assuming they're in <h2> tags)
        titles = soup.find_all('h2')

        # Print each title
        for title in titles:
            print(title.get_text())
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# URL of the website to scrape
url = 'https://example.com/articles'
scrape_titles(url)
