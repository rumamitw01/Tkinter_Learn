from tkinter import *
from random import *
def display():
    global status
    if Flag:
        if ball.get()=="1":
            raceResult.set("恭喜你贏了，Ball 1勝利")
        else:
            raceResult.set("抱歉你輸了，Ball 1勝利")
    else:
        if ball.get()=="1":
            raceResult.set("抱歉你輸了，Ball 2勝利")
        else:
            raceResult.set("恭喜你贏了，Ball 2勝利")
    startBtn.set("重置")
    status=False
def running():
    global Flag
    global status
    if startBtn.get()=="重置":
        startBtn.set("開始")
        raceResult.set("")
        canvas.delete("all")
    elif startBtn.get()=="開始":
        status=True
        canvas.create_text(10,50,text="1")
        id1=canvas.create_oval(20,50,70,100,fill="yellow")
        canvas.create_text(10,150,text="2")
        id2=canvas.create_oval(20,150,70,200,fill="aqua")
        id1Loc=0
        id2Loc=0
    if status==True:
        if ball.get()=="1" or ball.get()=="2":
            for x in range(100):
                if randint(1,100)>weight:
                    canvas.move(id2,5,0)
                    id2Loc+=1
                else:
                    canvas.move(id1,5,0)
                    id1Loc+=1
                tk.update()
                canvas.after(50)
            if id1Loc>id2Loc:
                Flag=True
            else:
                Flag=False
            display()
        else:
            raceResult.set("輸入錯誤！")
            return
tk=Tk()
canvas=Canvas(tk,width=500,height=250)
canvas.pack()

weight=60

Flag=True
status=False

frame=Frame(tk)
frame.pack(padx=5,pady=5)

Label(frame,text="哪一個球獲勝：").pack(side=LEFT)
ball=StringVar()
ball.set("1 or 2")
entry=Entry(frame,textvariable=ball).pack(side=LEFT,padx=3)
startBtn=StringVar()
startBtn.set("開始")
Button(frame,textvariable=startBtn,command=running).pack(side=LEFT)
raceResult=StringVar()

Label(frame,width=16,textvariable=raceResult).pack(side=LEFT,padx=3)

tk.mainloop()