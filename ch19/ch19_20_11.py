from tkinter import *

def inside_circle(xCenter,yCenter,radius,x,y):
    distance=((xCenter-x)**2+(yCenter-y)**2)**0.5
    if distance<=radius:
        return True
    else:
        return False
def is_inside(event):
    canvas.delete("text")
    if inside_circle(wd/2,ht/2,r,event.x,event.y):
        canvas.create_text(event.x,event.y-5,text="滑鼠游標在圓內",tags="text")
    else:
        canvas.create_text(event.x,event.y-5,text="滑鼠游標在圓外",tags="text")

window=Tk()
window.title("ch19_20_11")

wd=300
ht=240
r=100
canvas=Canvas(window,bg="yellow",width=wd,height=ht)
canvas.pack()
canvas.create_oval(wd/2-r,ht/2-r,wd/2+r,ht/2+r,tags="circle")
canvas.bind("<B1-Motion>",is_inside)
canvas.bind("<ButtonRelease-1>",lambda event:canvas.delete("text"))

window.mainloop()