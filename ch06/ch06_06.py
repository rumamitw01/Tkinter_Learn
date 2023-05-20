from tkinter import *
def callbackW(name,index,mode):
    xL.set(xE.get())
    print(f"name = '{name}', index = '{index}', mode = '{mode}'")


root=Tk()
root.title("ch06_06")

xE=StringVar()
entry=Entry(root,textvariable=xE)
entry.pack(padx=10,pady=5)
xE.trace("w",callbackW)

xL=StringVar()
label=Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(padx=10,pady=5)

root.mainloop()