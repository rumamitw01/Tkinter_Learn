from tkinter import *
from tkinter.ttk import *
import time

def running():
    while pb.cget("value")<=pb["maximum"]:
        pb.step(2)
        root.update()
        print(pb.cget("value"))
        time.sleep(0.05)

root=Tk()
root.title("ch15_04")

pb=Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"]=100
pb["value"]=0

btn=Button(root,text="Run",command=running)
btn.pack(pady=10)

root.mainloop()