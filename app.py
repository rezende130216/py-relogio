from tkinter import *
from tkinter import ttk
from time import strftime

root = Tk()
root.title("Relógio")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()
mainloop()