from tkinter import *
from tkinter import messagebox

def myMsg():
    messagebox.showinfo("My Message Box","Python tkinter早安")

window=Tk()
window.title("ch10_04")
window.geometry("300x160")

Button(window,text="Good Morning",command=myMsg).pack()

window.mainloop()