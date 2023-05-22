from tkinter import *

root=Tk()
root.title("ch13_03_01")
root.geometry("300x180")

omTuple=("Python","Java","C")
var=StringVar(root)
var.set(omTuple[0])
optionmenu=OptionMenu(root,var,*omTuple)
optionmenu.pack()

root.mainloop()