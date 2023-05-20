from tkinter import *
def enter(event):
    x.set("滑鼠進入Exit功能鈕")
def leave(event):
    x.set("滑鼠離開Exit功能鈕")

root=Tk()
root.title("ch11_03")
root.geometry("300x180")

btn=Button(root,text="離開",command=root.destroy)
btn.pack(pady=30)
btn.bind("<Enter>",enter)
btn.bind("<Leave>",leave)

x=StringVar()
lab=Label(root,textvariable=x,bg="yellow",fg="blue",height=4,width=18,font="Times 12 bold")
lab.pack(pady=30)

root.mainloop()