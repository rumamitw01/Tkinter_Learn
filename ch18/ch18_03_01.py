from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch18_03_01")

list1=["芝加哥","800"]
list2=["洛杉磯","1000"]
list3=["南京","900"]

tree=Treeview(root,columns=("cities","populations"))

tree.heading("#0",text="State")
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")

tree.insert("",index=END,text="伊利諾",values=list1)
tree.insert("",index=END,text="加州",values=list2)
tree.insert("",index=END,text="江蘇",values=list3)
tree.pack()

tree.mainloop()