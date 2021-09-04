from tkinter import Tk
from tkinter import Label
import time

root=Tk()
root.title("Shelley's Clock")

def Present_Time():
    display_time=time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(100, Present_Time)


digi_clock=Label(root,font=("Bookman Old Style",100),bg="Purple",fg="Yellow")
digi_clock.pack()

Present_Time()

root.mainloop()
