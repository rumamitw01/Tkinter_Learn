from tkinter import *
from tkinter.ttk import *
def treeSelect(event):
    widgetObj=event.widget
    itemSelected=widgetObj.selection()[0]
    col1=widgetObj.item(itemSelected,"text")
    col2=widgetObj.item(itemSelected,"values")[0]
    str=f"{col1}:{col2}"
    var.set(str)

root=Tk()
root.title("ch18_09")

stateCity={"伊利諾":"芝加哥","加州":"洛杉磯","德州":"休士頓","華盛頓州":"西雅圖","江蘇":"南京","山東":"青島","廣東":"廣州","福建":"廈門"}

tree=Treeview(root,columns=("cities"),selectmode=BROWSE)

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
tree.bind("<<TreeviewSelect>>",treeSelect)
tree.pack()

var=StringVar()
label=Label(root,textvariable=var,relief="groove")
label.pack(fill=BOTH,expand=True)

root.mainloop()