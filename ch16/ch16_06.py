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
def aboutMe():
    messagebox.showinfo("About Me","琉見著")

root=Tk()
root.title("ch16_06")
root.geometry("300x180")

menubar=Menu(root)
filemenu=Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu,underline=0)

filemenu.add_command(label="New File",command=newFile,underline=0)
filemenu.add_command(label="Open File",command=openFile,underline=0)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile,underline=0)
filemenu.add_command(label="Save As",command=saveAsFile,underline=5)
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)

helpmenu=Menu(menubar)
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)

helpmenu.add_command(label="About me",command=aboutMe,underline=1)

root.config(menu=menubar)

root.mainloop()