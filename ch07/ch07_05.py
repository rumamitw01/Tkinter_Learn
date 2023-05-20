from tkinter import *
def printSelection():
    label.config(text="你選的是"+var.get())

root=Tk()
root.title("ch07_05")

imgStar=PhotoImage(file="star.gif")
imgMoon=PhotoImage(file="moon.gif")
imgSun=PhotoImage(file="sun.gif")

var=StringVar()
var.set("星星")

label=Label(root,text="這是預設，尚未選擇",bg="lightyellow",width=30)
label.pack()

rbStar=Radiobutton(root,image=imgStar,variable=var,value="星星",command=printSelection)
rbStar.pack()
rbMoon=Radiobutton(root,image=imgMoon,variable=var,value="月亮",command=printSelection)
rbMoon.pack()
rbSun=Radiobutton(root,image=imgSun,variable=var,value="太陽",command=printSelection)
rbSun.pack()

root.mainloop()