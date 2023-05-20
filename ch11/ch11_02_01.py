from tkinter import *
def mouseMotion(event):
    x=event.x
    y=event.y
    textVar=f"Mouse Location - x:{x}, y:{y}"
    var.set(textVar)

root=Tk()
root.title("ch11_02_01")
root.geometry("300x180")

x,y=0,0
var=StringVar()
text=f"Mouse Location - x:{x}, y:{y}"
var.set(text)

lab=Label(root,textvariable=var)
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)
root.bind("<Motion>",mouseMotion)

root.mainloop()