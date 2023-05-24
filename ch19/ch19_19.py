from tkinter import *
import time
import random

tk=Tk()
canvas=Canvas(tk,width=500,height=250)
canvas.pack()
id1=canvas.create_oval(10,50,60,100,fill="yellow")
id2=canvas.create_oval(10,150,60,200,fill="aqua")
for x in range(100):
    if random.randint(1,100)>70:
        canvas.move(id2,5,0)
    else:
        canvas.move(id1,5,0)
    tk.update()
    time.sleep(0.05)