from tkinter import *
from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","開新檔案")

root=Tk()
root.title("ch16_02")
root.geometry("300x180")

menubar=Menu(root)
filemenu=Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)

root.mainloop()