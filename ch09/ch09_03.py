from tkinter import *

def printInfo():
    print(f"垂直捲軸值 = {sV.get()}, 水平捲軸值 = {sH.get()}")

root=Tk()
root.title("ch09_03")

sV=Scale(root,label="垂直",from_=0,to=10)
sV.set(5)
sV.pack()

sH=Scale(root,label="水平",from_=0,to=10,length=300,orient=HORIZONTAL)
sH.set(3)
sH.pack()

Button(root,text="Print",command=printInfo).pack()

root.mainloop()