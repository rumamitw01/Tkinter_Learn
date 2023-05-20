from tkinter import *
import random

def do_shuffle():
    random.shuffle(gifList)
    for i in range(3):
        labelList[i]["image"]=gifList[i]

window=Tk()
window.title("ch08_14")

gifList=[]
for i in range(1,8):
    gifList.append(PhotoImage(file="bookfigures/"+str(i)+".gif"))

frame=Frame(window)
frame.pack()

labelList=[]
for i in range(3):
    labelList.append(Label(frame,image=gifList[i]))
    labelList[i].pack(side=LEFT)

Button(window,text="重新顯示",command=do_shuffle).pack(pady=5)

window.mainloop()