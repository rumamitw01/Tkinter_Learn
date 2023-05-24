from tkinter import *
import math

def show_pendulum():
    global angle
    x1=wd/2
    y1=ht/2
    angle+=delta
    x=x1+pendulum_radius*math.cos(math.radians(angle))
    y=y1+pendulum_radius*math.sin(math.radians(angle))
    canvas.create_line(x1,y1,x,y,fill="goldenrod",tags="pendulum")
    canvas.create_oval(x1-r,y1-r,x1+r,y1+r,fill="gold",outline="gold",tags="pendulum")
    canvas.create_oval(x-radius,y-radius,x+radius,y+radius,fill="gold",outline="gold",tags="pendulum")

wd=300
ht=300
r=2
radius=10
pendulum_radius=ht*0.45
left_Angle=120
right_Angle=60
delta=3

window=Tk()
window.title("ch19_20_09")

canvas=Canvas(window,bg="blue",width=wd,height=ht)
canvas.pack()

angle=left_Angle
delay=30

while True:
    canvas.delete("pendulum")
    show_pendulum()
    canvas.after(delay)
    canvas.update()

window.mainloop()