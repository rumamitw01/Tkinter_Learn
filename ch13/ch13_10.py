from tkinter import *
from tkinter.ttk import *
def comboSelection(event):
    labelVar.set(var.get())

root=Tk()
root.title("ch13_10")
root.geometry("300x120")

var=StringVar()
cb=Combobox(root,textvariable=var)
cb["value"]=("Python","Java","C#","C")
cb.current(0)
cb.bind("<<ComboboxSelected>>",comboSelection)
cb.pack(side=LEFT,padx=10,pady=10)

labelVar=StringVar()
label=Label(root,textvariable=labelVar)
labelVar.set(var.get())
label.pack(side=LEFT)

root.mainloop()