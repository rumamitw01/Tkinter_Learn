from tkinter import *
def callback(*args):
    print("data changed : ",xE.get())

root=Tk()
root.title("ch06_03")

xE=StringVar()
entry=Entry(root,textvariable=xE)
entry.pack(padx=10,pady=5)
xE.trace("w",callback)

root.mainloop()