from tkinter import *
from tkinter.ttk import *

def run():
    pb.start()
def stop():
    pb.stop()

root=Tk()
root.title("ch15_06")

pb=Progressbar(root,length=200,mode="indeterminate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"]=100
pb["value"]=0

btnRun=Button(root,text="Run",command=run)
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop=Button(root,text="Stop",command=stop)
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()