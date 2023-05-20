from tkinter import *

root=Tk()
root.title("ch08_07")

msg="歡迎進入Silicon Stone Eduction系統"
sseGif=PhotoImage(file="sse.gif")
logo=Label(root,image=sseGif,text=msg,compound=BOTTOM)
logo.pack()

labFrame=LabelFrame(root,text="資料驗證")
accountL=Label(labFrame,text="Account")
accountL.grid(row=1)
pwdL=Label(labFrame,text="Password")
pwdL.grid(row=2)

accountE=Entry(labFrame)
pwdE=Entry(labFrame,show="*")
accountE.grid(row=1,column=1)
pwdE.grid(row=2,column=1,pady=10)
labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)

root.mainloop()