from tkinter import *

window=Tk()
window.title("ch03_16")

lab1=Label(window,text="明志科技大學",bg="lightyellow")
lab2=Label(window,text="長庚大學",bg="lightgreen")
lab3=Label(window,text="長庚科技大學",bg="lightblue")

lab1.pack(side=LEFT)
lab2.pack()
lab3.pack()

window.mainloop()