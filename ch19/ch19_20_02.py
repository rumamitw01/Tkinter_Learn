from tkinter import *
import time
def mouseMotion(event):
    x,y=event.x,event.y
    textvar=f"Mouse location - x:{x}, y:{y}"
    var.set(textvar)

root=Tk()
root.title("ch19_20_02")
root.geometry("300x180")

x,y=0,0
var=StringVar()
text=f"Mouse location - x:{x}, y:{y}"
var.set(text)

lab=Label(root,textvariable=var)
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)

root.bind("<Motion>",mouseMotion)

root.mainloop()