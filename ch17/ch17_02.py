from tkinter import *

root=Tk()
root.title("ch17_02")

text=Text(root,height=3,width=30)
text.pack()
text.insert(END,"Python王者歸來\nJava王者歸來\n")
text.insert(INSERT,"深智數位公司")

root.mainloop()