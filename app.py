from tkinter import *
from tkinter import ttk
import os
import time

def shutDown():
    global entry
    global pcShutDownText
    global popText
    global minutesText
    
    minutes= entry.get()
    pcShutDownText.pack()
    popText.configure(text=minutes)
    popText.pack()
    minutesText.pack()
    convertedMinutes = int(minutes)*60
    os.system(f'shutdown /s /t {convertedMinutes}')

root = Tk()
root.title("Shutdown Timer")
root.configure(bg='white')
root.geometry('350x400')
root.resizable(False, False)

s = ttk.Style()
s.theme_names()
s.theme_use('clam')

#Initialize a Label to display the User Input
Label(root, text="Shutdown Timer", font=("Helvetica 24 bold"), padx= 10, pady=20, background="red", fg="white", width="100").pack()
Label(root, text="Set Shutdown Timer (minutes):", font=("Helvetica 16"), background='white', pady=20).pack()

#Initialize a Entry Widget to take the input from the User
entry = Entry(root, width=20, font=("Helvetica 16"))
entry.pack(pady=15)

Button(root, text="Set Time", command=shutDown, bg='#000', fg='#ffffff', bd=0, height=2, width=15, font=("Helvetica 11")).pack()

pcShutDownText = Label(root, text="Your PC will shutdown after", font=("Helvetica 14"), background='white', padx= 10, pady=15, width="100")

popText = Label(root, text="", font=("Helvetica 20"), background='white', fg="red")

minutesText = Label(root, text="minutes", font=("Helvetica 14"), background='white', padx= 10, pady=15, width="100")

root.mainloop()