from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
def msg():
    messagebox.showinfo("Notebook","歡迎使用Notebook")

root=Tk()
root.title("ch14_07")
root.geometry("300x160")

notebook=Notebook(root)

frame1=Frame()
frame2=Frame()

label=Label(frame1,text="Python")
label.pack(padx=10,pady=10)
btn=Button(frame2,text="Help",command=msg)
btn.pack(padx=10,pady=10)

notebook.add(frame1,text="頁次1")
notebook.add(frame2,text="頁次2")
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()