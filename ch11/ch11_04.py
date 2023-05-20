from tkinter import *
from tkinter import messagebox

def leave(event):
    ret=messagebox.askyesno("ch11_04","是否離開？")
    if ret==True:
        root.destroy()
    else:
        return

root=Tk()
root.title("ch11_04")

root.bind("<Escape>",leave)
lab=Label(root,text="測試Esc鍵",bg="yellow",fg="blue",height=4,width=15,font="Times 12 bold")
lab.pack(padx=30,pady=30)

root.mainloop()