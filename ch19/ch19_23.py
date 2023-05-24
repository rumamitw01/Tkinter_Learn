from tkinter import *
from random import *
import time

class Ball:
    def __init__(self,canvas,color,winW,winH):
        self.canvas=canvas
        self.id=canvas.create_oval(0,0,20,20,fill=color)
        self.canvas.move(self.id,winW/2,winH/2)
        self.x=0
        self.y=step
    def ballMove(self):
        self.canvas.move(self.id,self.x,self.y)
        ballPos=self.canvas.coords(self.id)
        if ballPos[1]<=0:
            self.y=step
        if ballPos[3]>=winH:
            self.y=-step

winW=640
winH=480
step=3
speed=0.03

tk=Tk()
tk.title("Bouncing Ball")
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=winW,height=winH)
canvas.pack()
tk.update()

ball=Ball(canvas,"yellow",winW,winH)

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)