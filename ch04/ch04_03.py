from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")

root=Tk()
root.title("ch04_03")
label=Label(root)
btn1=Button(root,text="列印訊息",command=msgShow)
btn2=Button(root,text="結束",command=root.destroy)
label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

root.mainloop()