from tkinter import *
def callback(*args):
    xL.set(xE.get())
    print("data changed : ",xE.get())

root=Tk()
root.title("ch06_04")

xE=StringVar()
entry=Entry(root,textvariable=xE)
entry.pack(padx=10,pady=5)
xE.trace("w",callback)

xL=StringVar()
label=Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(padx=10,pady=5)

root.mainloop()