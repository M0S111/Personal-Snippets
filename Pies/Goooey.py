import tkinter as tk
from DRClever import digitRoot as dR
#from tkinter import *
#from tkinter.ttk import *

window = tk.Tk()

window.title("Digital Root Calculator")

frame = tk.Frame()

prompt = tk.Label(master=frame,text='Enter your number to calculate digital root here:',
                 width=50)

field = tk.Entry(master=frame,width=10)

def show():
    prompt["text"] = f"The digital root of {field.get()} is: {dR(field.get())}"

submit = tk.Button(master=frame,text='Submit',command=show)

prompt.pack()

field.pack()

submit.pack()

frame.pack()

window.mainloop()
