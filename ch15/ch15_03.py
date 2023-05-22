from tkinter import *
from tkinter.ttk import *

def load():
    pb["value"]=0
    pb["maximum"]=maxbytes
    loading()
def loading():
    global bytes
    bytes+=500
    pb["value"]=bytes
    if bytes<maxbytes:
        pb.after(50,loading)

root=Tk()
root.title("ch15_03")
bytes=0
maxbytes=10000

pb=Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"]=0

btn=Button(root,text="Load",command=load)
btn.pack(pady=10)

root.mainloop()