from tkinter import *
import time
def callback(event):
    print("Clicked at",event.x,event.y)

root=Tk()
root.title("ch19_20_01")
canvas=Canvas(root,width=300,height=180)
canvas.pack()
canvas.bind_all("<Button-1>",callback)

mainloop()