from tkinter import *

tk=Tk()
canvas=Canvas(tk,width=500,height=300)
canvas.pack()
canvas.create_oval(10,50,60,100,fill="yellow",outline="lightgray")
for x in range(80):
    canvas.move(1,5,2)
    tk.update()
    canvas.after(50)