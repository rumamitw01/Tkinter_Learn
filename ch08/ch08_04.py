from tkinter import *

root=Tk()
root.title("ch08_04")

fm1=Frame(width=150,height=80,relief=GROOVE,borderwidth=5)
fm1.pack(side=LEFT,padx=5,pady=10)

fm2=Frame(width=150,height=80,relief=RAISED,borderwidth=5)
fm2.pack(side=LEFT,padx=5,pady=10)

fm3=Frame(width=150,height=80,relief=RIDGE,borderwidth=5)
fm3.pack(side=LEFT,padx=5,pady=10)

root.mainloop()