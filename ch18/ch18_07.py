from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch18_07")

asia={"中國":"北京","日本":"東京","泰國":"曼谷","韓國":"首爾"}
euro={"英國":"倫敦","法國":"巴黎","德國":"柏林","挪威":"奧斯陸"}

tree=Treeview(root,columns=("capital"))

tree.heading("#0",text="國家")
tree.heading("capital",text="首都")

idAsia=tree.insert("",index=END,text="Asia")
idEuro=tree.insert("",index=END,text="Europe")

for country in asia.keys():
    tree.insert(idAsia,index=END,text=country,values=asia[country])
for country in euro.keys():
    tree.insert(idEuro,index=END,text=country,values=euro[country])
tree.pack()

tree.mainloop()