from tkinter import *
from tkinter.ttk import *
def removeItem():
    ids=tree.selection()
    for id in ids:
        tree.delete(id)
def insertItem():
    state=stateEntry.get()
    city=cityEntry.get()
    if len(state.strip())==0 or len(city.strip())==0:
        return
    tree.insert("",END,text=state,values=city)
    stateEntry.delete(0,END)
    cityEntry.delete(0,END)

root=Tk()
root.title("ch18_11")

stateCity={"伊利諾":"芝加哥","加州":"洛杉磯","德州":"休士頓","華盛頓州":"西雅圖","江蘇":"南京","山東":"青島","廣東":"廣州","福建":"廈門"}

root.rowconfigure(1,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(3,weight=1)

stateLab=Label(root,text="State :")
stateLab.grid(row=0,column=0,padx=5,pady=3,sticky=W)
stateEntry=Entry()
stateEntry.grid(row=0,column=1,sticky=W+E,padx=5,pady=3)
cityLab=Label(root,text="City :")
cityLab.grid(row=0,column=2,sticky=E)
cityEntry=Entry()
cityEntry.grid(row=0,column=3,sticky=W+E,padx=5,pady=3)

inBtn=Button(root,text="插入",command=insertItem)
inBtn.grid(row=0,column=4,padx=5,pady=3)

tree=Treeview(root,columns=("cities"),selectmode=EXTENDED)

tree.heading("#0",text="State")
tree.heading("cities",text="City")

tree.column("cities",anchor=CENTER)

for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.grid(row=1,column=0,columnspan=5,padx=5,sticky=W+E+N+S)

rmBtn=Button(root,text="Remove",command=removeItem)
rmBtn.grid(row=2,column=2,padx=5,pady=3,sticky=W)

root.mainloop()