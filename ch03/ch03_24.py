from tkinter import *

window=Tk()
window.title("ch03_24")

lab1=Label(window,text="明志科技大學",bg="lightyellow",width=15)
lab2=Label(window,text="長庚大學",bg="lightgreen",width=15)
lab3=Label(window,text="長庚科技大學",bg="lightblue",width=15)

lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
lab3.grid(row=1,column=1)

window.mainloop()