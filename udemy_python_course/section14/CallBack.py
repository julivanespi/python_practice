from tkinter import *
from tkinter import ttk

def BuClick():
    print("Button is clicked!")


root=Tk()

bu = ttk.Button(root, text="Click me!", command = BuClick).pack()

root.mainloop()