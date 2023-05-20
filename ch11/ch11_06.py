from tkinter import *
def key(event):
    print("按了"+repr(event.char)+"鍵")

def coordXY(event):
    frame.focus_set()
    print("滑鼠座標：",event.x,event.y)

root=Tk()
root.title("ch11_06")

frame=Frame(root,width=100,height=100)
frame.bind("<Key>",key)
frame.bind("<Button-1>",coordXY)
frame.pack()

root.mainloop()