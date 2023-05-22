from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch13_06")
root.geometry("300x120")

var=StringVar()
cb=Combobox(root,textvariable=var)
cb["value"]=("Python","Java","C#","C")
cb.pack(pady=10)

root.mainloop()