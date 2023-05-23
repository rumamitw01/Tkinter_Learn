from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch18_06")

stateCity={"伊利諾":"芝加哥","加州":"洛杉磯","德州":"休士頓","華盛頓州":"西雅圖","江蘇":"南京","山東":"青島","廣東":"廣州","福建":"廈門"}

tree=Treeview(root,columns=("cities"))

tree.heading("#0",text="State")
tree.heading("cities",text="City")

tree.column("cities",anchor=CENTER)

tree.tag_configure("evenColor",background="lightblue")

rowCount=1
for state in stateCity.keys():
    if rowCount%2==1:
        tree.insert("",index=END,text=state,values=stateCity[state])
    else:
        tree.insert("",index=END,text=state,values=stateCity[state],tags=("evenColor"))
    rowCount+=1
tree.pack()

tree.mainloop()