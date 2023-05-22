from tkinter import *
def printSelection():
    print("The selection is :",var.get())

root=Tk()
root.title("ch13_04")
root.geometry("300x180")

omTuple=("Python","Java","C")
var=StringVar(root)
var.set("Python")
optionmenu=OptionMenu(root,var,*omTuple)
optionmenu.pack(pady=10)

btn=Button(root,text="Print",command=printSelection)
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()