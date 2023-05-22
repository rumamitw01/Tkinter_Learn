from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch13_07")
root.geometry("300x120")

var=StringVar()
cb=Combobox(root,textvariable=var)
cb["value"]=("Python","Java","C#","C")
cb.current(0)
cb.pack(pady=10)

root.mainloop()