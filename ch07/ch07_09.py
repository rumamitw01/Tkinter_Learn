from tkinter import *

def selAll():
    entry.select_range(0,END)
def deSel():
    entry.select_clear()
def clr():
    entry.delete(0,END)
def readonly():
    if var.get()==True:
        entry.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)

root=Tk()
root.title("ch07_09")

entry=Entry(root)
entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=W)

btnSel=Button(root,text="選取",command=selAll)
btnSel.grid(row=1,column=0,padx=5,pady=5,sticky=W)
btnSel=Button(root,text="取消選取",command=deSel)
btnSel.grid(row=1,column=1,padx=5,pady=5,sticky=W)
btnSel=Button(root,text="刪除",command=clr)
btnSel.grid(row=1,column=2,padx=5,pady=5,sticky=W)
btnSel=Button(root,text="結束",command=root.destroy)
btnSel.grid(row=1,column=3,padx=5,pady=5,sticky=W)

var=BooleanVar()
var.set(False)
chkReadonly=Checkbutton(root,text="唯讀",variable=var,command=readonly)
chkReadonly.grid(row=2,column=0)

root.mainloop()