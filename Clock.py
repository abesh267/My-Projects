from tkinter import *
from tkinter.ttk import *

from time import strftime

gui = Tk()
gui.title("Clock")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

label = Label(gui,font=("new times roman",75),background="black",foreground="red")
label.pack(anchor="center")
time()
mainloop()