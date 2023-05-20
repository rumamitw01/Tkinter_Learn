from tkinter import *
def printSelection():
    num=var.get()
    if num==1:
        label.config(text="你是男生")
    else:
        label.config(text="你是女生")

root=Tk()
root.title("ch07_01")

var=IntVar()
var.set(1)

label=Label(root,text="這是預設，尚未選擇")
label.pack()

rbman=Radiobutton(root,text="男生",variable=var,value=1,command=printSelection)
rbman.pack()
rbwoman=Radiobutton(root,text="女生",variable=var,value=2,command=printSelection)
rbwoman.pack()

root.mainloop()