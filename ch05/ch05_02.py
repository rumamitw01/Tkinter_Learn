from tkinter import *

root=Tk()
root.title("ch05_02")

accountL=Label(root,text="Account")
accountL.grid(row=0)
pwdL=Label(root,text="Password")
pwdL.grid(row=1)

accountE=Entry(root)
pwdE=Entry(root,show="*")
accountE.grid(row=0,column=1)
pwdE.grid(row=1,column=1)

root.mainloop()