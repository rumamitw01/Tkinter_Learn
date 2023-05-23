from tkinter import *
from tkinter.ttk import *
def removeItem():
    iids=tree.selection()
    for iid in iids:
        tree.delete(iid)

root=Tk()
root.title("ch18_10")

stateCity={"伊利諾":"芝加哥","加州":"洛杉磯","德州":"休士頓","華盛頓州":"西雅圖","江蘇":"南京","山東":"青島","廣東":"廣州","福建":"廈門"}

tree=Treeview(root,columns=("cities"),selectmode=EXTENDED)

tree.heading("#0",text="State")
tree.heading("cities",text="City")

tree.column("cities",anchor=CENTER)

for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.pack()

rmBtn=Button(root,text="Remove",command=removeItem)
rmBtn.pack(pady=5)

root.mainloop()