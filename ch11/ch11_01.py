from tkinter import *
def pythonClicked():
    if varPython.get():
        lab.config(text="選取Python")
    else:
        lab.config(text="取消選取Python")
def javaClicked():
    if varJava.get():
        lab.config(text="選取Java")
    else:
        lab.config(text="取消選取Java")
def buttonClicked():
    lab.config(text="Button clicked")

root=Tk()
root.title("ch11_01")
root.geometry("300x180")

btn=Button(root,text="Click Me",command=buttonClicked)
btn.pack(anchor=W)
varPython=BooleanVar()
cbnPython=Checkbutton(root,text="Python",variable=varPython,command=pythonClicked)
cbnPython.pack(anchor=W)
varJava=BooleanVar()
cbnJava=Checkbutton(root,text="Java",variable=varJava,command=javaClicked)
cbnJava.pack(anchor=W)
lab=Label(root,bg="yellow",fg="blue",height=2,width=12,font="Times 16 bold")
lab.pack()

root.mainloop()