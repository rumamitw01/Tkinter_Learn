from tkinter import *

root=Tk()
root.title("ch08_05")

fm=Frame(width=150,height=80,relief=RAISED,borderwidth=5)
lab=Label(fm,text="請複選常用的程式語言")
lab.pack()
python=Checkbutton(fm,text="Python")
python.pack(anchor=W)
java=Checkbutton(fm,text="Java")
java.pack(anchor=W)
ruby=Checkbutton(fm,text="Ruby")
ruby.pack(anchor=W)
fm.pack(padx=10,pady=10)

root.mainloop()