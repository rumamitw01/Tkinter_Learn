from tkinter import *

def printInfo():
    print(sp.get())

root=Tk()
root.title("ch09_07")

sp=Spinbox(root,from_=0,to=10,command=printInfo)
sp.pack(padx=10,pady=10)

root.mainloop()