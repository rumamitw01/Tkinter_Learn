from tkinter import *
from tkinter.ttk import *
def printSelection():
    print(var.get())

root=Tk()
root.title("ch13_09")
root.geometry("300x120")

var=StringVar()
cb=Combobox(root,textvariable=var)
cb["value"]=("Python","Java","C#","C")
cb.current(0)
cb.pack(pady=10)

btn=Button(root,text="Print",command=printSelection)
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()