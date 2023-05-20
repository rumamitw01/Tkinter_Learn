from tkinter import *

def btn_hit():
    global msg_on
    if msg_on==False:
        msg_on=True
        x.set("I like tkinter")
    else:
        msg_on=False
        x.set("")

root=Tk()
root.title("ch06_01")

msg_on=False
x=StringVar()

label=Label(root,textvariable=x,fg="blue",bg="lightyellow",font="Verdana 16 bold",width=25,height=2)
label.pack()
btn=Button(root,text="Click Me",command=btn_hit)
btn.pack()

root.mainloop()