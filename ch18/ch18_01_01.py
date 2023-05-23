from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch18_01_01")

tree=Treeview(root,columns=("cities"),show="headings")

tree.heading("#0",text="State")
tree.heading("#1",text="City")

tree.insert("",index=END,text="伊利諾",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉磯")
tree.insert("",index=END,text="江蘇",values="南京")
tree.pack()

tree.mainloop()