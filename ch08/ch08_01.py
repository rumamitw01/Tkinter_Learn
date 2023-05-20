from tkinter import *

root=Tk()
root.title("ch08_01")

for fm in ["red","green","blue"]:
    Frame(root,bg=fm,height=50,width=250).pack()

root.mainloop()