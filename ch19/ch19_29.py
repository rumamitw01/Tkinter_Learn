from tkinter import *
import random

def getColor():
    colorlist=["red","green","blue","aqua","gold","purple"]
    return random.choice(colorlist)

class Ball:
    def __init__(self):
        self.x=width/2
        self.y=0
        self.dx=3
        self.dy=3
        self.radius=5
        self.color=getColor()

def addBall():
    ballList.append(Ball())
def removeBall():
    ballList.pop()
def stop():
    global ballRunning
    ballRunning=True
def resume():
    global ballRunning
    ballRunning=False
    animate()
def animate():
    global ballRunning
    while not ballRunning:
        canvas.after(sleepTime)
        canvas.update()
        canvas.delete("ball")
        for ball in ballList:
            redisplayBall(ball)
def redisplayBall(ball):
    if ball.x>width or ball.x<0:
        ball.dx=-ball.dx
    if ball.y>height or ball.y<0:
        ball.dy=-ball.dy
    ball.x+=ball.dx
    ball.y+=ball.dy
    canvas.create_oval(ball.x-ball.radius,ball.y-ball.radius,ball.x+ball.radius,ball.y+ball.radius,fill=ball.color,tags="ball")

tk=Tk()
tk.title("ch19_29")
ballList=[]
width,height=400,260
canvas=Canvas(tk,width=width,height=height)
canvas.pack()

frame=Frame(tk)
frame.pack()
btnStop=Button(frame,text="暫停",command=stop)
btnStop.pack(side=LEFT)
btnResume=Button(frame,text="恢復",command=resume)
btnResume.pack(side=LEFT)
btnAdd=Button(frame,text="增加球",command=addBall)
btnAdd.pack(side=LEFT)
btnRemove=Button(frame,text="減少球",command=removeBall)
btnRemove.pack(side=LEFT)
btnExit=Button(frame,text="結束",command=tk.destroy)
btnExit.pack(side=LEFT)

sleepTime=50
ballRunning=False
animate()

tk.mainloop()