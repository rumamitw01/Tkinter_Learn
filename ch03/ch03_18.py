from tkinter import *

window=Tk()
window.title("ch03_18")

lab1=Label(window,text="明志科技大學",bg="lightyellow")
lab2=Label(window,text="長庚大學",bg="lightgreen")
lab3=Label(window,text="長庚科技大學",bg="lightblue")

lab1.pack(side=LEFT,fill=Y)
lab2.pack(fill=X)
lab3.pack(fill=X)

window.mainloop()