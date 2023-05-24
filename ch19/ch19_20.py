from tkinter import *
import time
def ballMove(event):
    if event.keysym=="Left":
        canvas.move(1,-5,0)
    if event.keysym=="Right":
        canvas.move(1,5,0)
    if event.keysym=="Up":
        canvas.move(1,0,-5)
    if event.keysym=="Down":
        canvas.move(1,0,5)
tk=Tk()
canvas=Canvas(tk,width=500,height=300)
canvas.pack()
canvas.create_oval(225,125,275,175,fill="red")
canvas.bind_all("<KeyPress-Left>",ballMove)
canvas.bind_all("<KeyPress-Right>",ballMove)
canvas.bind_all("<KeyPress-Up>",ballMove)
canvas.bind_all("<KeyPress-Down>",ballMove)
mainloop()