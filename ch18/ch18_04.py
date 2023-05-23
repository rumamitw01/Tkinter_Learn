from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch18_04")

tree=Treeview(root,columns=("cities","populations"))

tree.heading("#0",text="State")
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")

tree.column("#1",anchor=CENTER,width=150)
tree.column("#2",anchor=CENTER,width=150)

tree.insert("",index=END,text="伊利諾",values=("芝加哥","800"))
tree.insert("",index=END,text="加州",values=("洛杉磯","1000"))
tree.insert("",index=END,text="江蘇",values=("南京","900"))
tree.pack()

tree.mainloop()