from tkinter import *
def Draw_Line(event):
    global x
    global y
    if event.keysym=="Left":
        canvas.create_line(x,y,x-5,y)
        x-=5
    if event.keysym=="Right":
        canvas.create_line(x,y,x+5,y)
        x+=5
    if event.keysym=="Up":
        canvas.create_line(x,y,x,y-5)
        y-=5
    if event.keysym=="Down":
        canvas.create_line(x,y,x,y+5)
        y+=5

xWidth=200
yHeight=200

window=Tk()
window.title("ch19_20_05")

canvas=Canvas(window,width=xWidth,height=yHeight)
canvas.pack()

x=xWidth/2
y=yHeight/2

canvas.bind_all("<KeyPress-Left>",Draw_Line)
canvas.bind_all("<KeyPress-Right>",Draw_Line)
canvas.bind_all("<KeyPress-Up>",Draw_Line)
canvas.bind_all("<KeyPress-Down>",Draw_Line)
canvas.focus_set()

window.mainloop()