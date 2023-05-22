from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")

root=Tk()
root.title("ch16_07")
root.geometry("300x180")

menubar=Menu(root)
filemenu=Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
filemenu.add_command(label="New File",command=newFile,accelerator="Ctrl+N")
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)
root.config(menu=menubar)

root.bind("<Control-n>",lambda event:messagebox.showinfo("New File","開新檔案"))

root.mainloop()