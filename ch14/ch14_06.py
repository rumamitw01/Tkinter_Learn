from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch14_06")
root.geometry("300x160")

notebook=Notebook(root)

frame1=Frame()
frame2=Frame()

notebook.add(frame1,text="頁次1")
notebook.add(frame2,text="頁次2")
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()