from tkinter import *

def msgShow():
    label.config(text="I love Python",bg="lightyellow",fg="blue")

root=Tk()
root.title("ch04_11")
label=Label(root)

sunGif=PhotoImage(file="sun.gif")
btn=Button(root,image=sunGif,command=msgShow,cursor="star")
label.pack()
btn.pack()

root.mainloop()