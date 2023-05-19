from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")

root=Tk()
root.title("ch04_02")
label=Label(root)
btn=Button(root,text="列印訊息",command=msgShow)
label.pack()
btn.pack()

root.mainloop()