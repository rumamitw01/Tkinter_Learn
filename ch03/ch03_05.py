from tkinter import *

Reliefs=["flat","groove","raised","ridge","solid","sunken"]

root=Tk()
root.title("ch03_05")

for Relief in Reliefs:
    Label(root,text=Relief,relief=Relief,fg="blue",font="Times 20 bold").pack(side=LEFT,padx=5)

root.mainloop()