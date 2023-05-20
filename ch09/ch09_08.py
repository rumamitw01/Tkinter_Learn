from tkinter import *

def printInfo():
    print(sp.get())

root=Tk()
root.title("ch09_08")

sp=Spinbox(root,values=(10,38,170,101),command=printInfo)
sp.pack(padx=10,pady=10)

root.mainloop()