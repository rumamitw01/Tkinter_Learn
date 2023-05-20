from tkinter import *
def callbackW(*args):
    xL.set(xE.get())

def callbackR(*args):
    print("Warning:資料被讀取!")

def hit():
    print("讀取資料:",xE.get())

root=Tk()
root.title("ch06_05")

xE=StringVar()
entry=Entry(root,textvariable=xE)
entry.pack(padx=10,pady=5)
xE.trace("w",callbackW)
xE.trace("r",callbackR)

xL=StringVar()
label=Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(padx=10,pady=5)

btn=Button(root,text="讀取",command=hit)
btn.pack(pady=5)

root.mainloop()