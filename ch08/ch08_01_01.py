from tkinter import *

root=Tk()
root.title("ch08_01_01")

for fm in ["red","green","blue"]:
    Frame(bg=fm,height=50,width=250).pack()

root.mainloop()