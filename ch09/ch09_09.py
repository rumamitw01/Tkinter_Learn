from tkinter import *

def printInfo():
    print(sp.get())

root=Tk()
root.title("ch09_09")
cities=("新加坡","上海","東京")

sp=Spinbox(root,values=cities,command=printInfo)
sp.pack(padx=10,pady=10)

root.mainloop()