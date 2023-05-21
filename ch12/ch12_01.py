from tkinter import *

root=Tk()
root.title("ch12_01")
root.geometry("300x210")

lb1=Listbox(root)
lb1.pack(side=LEFT,padx=5,pady=10)
lb2=Listbox(root,height=5,relief="raised")
lb2.pack(anchor=N,side=LEFT,padx=5,pady=10)

root.mainloop()