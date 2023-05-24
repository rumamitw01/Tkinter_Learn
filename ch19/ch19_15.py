from tkinter import *
def paint(event):
    x1,y1=event.x,event.y
    x2,y2=event.x,event.y
    canvas.create_oval(x1,y1,x2,y2,fill="blue")
def cls():
    canvas.delete("all")
tk=Tk()
lab=Label(tk,text="拖曳滑鼠可以繪圖")
lab.pack()
canvas=Canvas(tk,width=640,height=300)
canvas.pack()

btn=Button(tk,text="清除",command=cls)
btn.pack(pady=5)

canvas.bind("<B1-Motion>",paint)

canvas.mainloop()