from tkinter import *

root=Tk()
root.title("ch08_02")

fms={"red":"cross","green":"boat","blue":"clock"}
for fmColor in fms:
    Frame(root,bg=fmColor,cursor=fms[fmColor],height=50,width=250).pack(side=LEFT)

root.mainloop()