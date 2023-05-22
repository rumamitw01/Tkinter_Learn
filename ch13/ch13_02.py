from tkinter import *

root=Tk()
root.title("ch13_02")
root.geometry("300x180")

omTuple=("Python","Java","C")
var=StringVar(root)
optionmenu=OptionMenu(root,var,*omTuple)
optionmenu.pack()

root.mainloop()