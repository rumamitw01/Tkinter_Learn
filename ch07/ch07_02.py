from tkinter import *
def printSelection():
    label.config(text="你是"+var.get())

root=Tk()
root.title("ch07_02")

var=StringVar()
var.set("男生")

label=Label(root,text="這是預設，尚未選擇")
label.pack()

rbman=Radiobutton(root,text="男生",variable=var,value="男生",command=printSelection)
rbman.pack()
rbwoman=Radiobutton(root,text="女生",variable=var,value="女生",command=printSelection)
rbwoman.pack()

root.mainloop()