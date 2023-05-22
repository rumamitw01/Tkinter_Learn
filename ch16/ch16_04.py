from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")
def openFile():
    messagebox.showinfo("Open File","開啟舊檔")
def saveFile():
    messagebox.showinfo("Save File","儲存檔案")
def saveAsFile():
    messagebox.showinfo("Save File As","另存新檔")

root=Tk()
root.title("ch16_04")
root.geometry("300x180")

menubar=Menu(root)
filemenu=Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Open File",command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)

root.mainloop()