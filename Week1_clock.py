from tkinter import *
from tkinter.ttk import *
from time import strftime

#define widows
myclock = Tk()
myclock.title("hello")

#define time
def time():
    string=strftime("%H:%M:%S %p")
    Label.config(text=string)
    Label.after(1000,time)

#show label
Label=Label(myclock)
Label.pack(anchor="center")

time()

mainloop()