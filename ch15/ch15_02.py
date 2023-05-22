from tkinter import *
from tkinter.ttk import *
import time

def running():
    for i in range(100):
        pb["value"]=i+1
        root.update()
        time.sleep(0.05)

root=Tk()
root.geometry("300x140")
root.title("ch15_02")

pb=Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(pady=20)
pb["maximum"]=100
pb["value"]=0

btn=Button(root,text="Run",command=running)
btn.pack(pady=10)

root.mainloop()