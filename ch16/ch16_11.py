from tkinter import *

root=Tk()
root.title("ch16_11")
root.geometry("300x180")

menubar=Menu(root)

filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="Exit",command=root.destroy)

toolbar=Frame(root,relief=RAISED,borderwidth=3)

sunGif=PhotoImage(file="sun.gif")
exitBtn=Button(toolbar,image=sunGif,command=root.destroy)
exitBtn.pack(side=LEFT,padx=3,pady=3)
toolbar.pack(side=TOP,fill=X)
root.config(menu=menubar)

root.mainloop()