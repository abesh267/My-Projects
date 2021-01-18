import random
from tkinter import *

gui = Tk()
gui.title("Dice Simulator")
gui.geometry("800x500")

label1 = Label(gui,font=("new times roman",200))

def roll():
    numbers = ["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    label1.config(text=f'{random.choice(numbers)}{random.choice(numbers)}')
    label1.pack()

button1 = Button(gui,text="Roll it!!!",command=roll)
button1.place(x=373,y=300) 

gui.mainloop()