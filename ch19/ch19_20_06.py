from tkinter import *
def displayFan(startingAngle):
    canvas.delete("fan")
    canvas.create_arc(xWidth/2-r,yHeight/2-r,xWidth/2+r,yHeight/2+r,start=startAngle,extent=60,fill="green",tags="fan")
    canvas.create_arc(xWidth/2-r,yHeight/2-r,xWidth/2+r,yHeight/2+r,start=startAngle+120,extent=60,fill="green",tags="fan")
    canvas.create_arc(xWidth/2-r,yHeight/2-r,xWidth/2+r,yHeight/2+r,start=startAngle+240,extent=60,fill="green",tags="fan")

xWidth=300
yHeight=300
r=120

window=Tk()
window.title("ch19_20_06")

canvas=Canvas(window,width=xWidth,height=yHeight)
canvas.pack()

startAngle=0
while True:
    startAngle+=5
    displayFan(startAngle)
    canvas.after(50)
    canvas.update()

window.mainloop()