from tkinter import *

window=Tk()
window.title("ch03_02")

lab1=Label(window,text="明志科技大學",bg="lightyellow",width=15)
lab2=Label(window,text="長庚大學",bg="lightgreen",width=15)
lab3=Label(window,text="長庚科技大學",bg="lightblue",width=15)

lab1.pack(side=BOTTOM)
lab2.pack(side=BOTTOM)
lab3.pack(side=BOTTOM)

window.mainloop()