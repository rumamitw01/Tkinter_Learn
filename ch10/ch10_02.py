from tkinter import *

root=Tk()
root.title("ch10_02")

var=StringVar()
msg=Message(root,textvariable=var,relief=RAISED)
var.set("2016年12月，我一個人訂了機票和船票，開始我的南極旅行")
msg.pack(padx=10,pady=10)

root.mainloop()