from tkinter import *
def callback(event):
    print("Clicked at",event.x,event.y)

root=Tk()
root.title("ch11_02")
frame=Frame(root,width=300,height=100)
frame.bind("<Button-1>",callback)
frame.pack()

root.mainloop()