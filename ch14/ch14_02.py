from tkinter import *

root=Tk()
root.title("ch14_02")

pw=PanedWindow(orient=HORIZONTAL)

leftframe=LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe)
middleframe=LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe)
rightframe=LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe)

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)

root.mainloop()