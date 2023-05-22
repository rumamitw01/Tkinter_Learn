from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch14_03")

pw=PanedWindow(orient=HORIZONTAL)

leftframe=LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe,weight=1)
middleframe=LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe,weight=1)
rightframe=LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe,weight=1)

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)

root.mainloop()