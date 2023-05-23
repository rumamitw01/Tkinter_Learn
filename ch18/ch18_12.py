from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
def doubleClick(event):
    e=event.widget
    iid=e.identify("item",event.x,event.y)
    state=e.item(iid,"text")
    city=e.item(iid,"value")[0]
    str=f"{state}:{city}"
    messagebox.showinfo("Double Clicked",str)

root=Tk()
root.title("ch18_12")

stateCity={"伊利諾":"芝加哥","加州":"洛杉磯","德州":"休士頓","華盛頓州":"西雅圖","江蘇":"南京","山東":"青島","廣東":"廣州","福建":"廈門"}

tree=Treeview(root,columns=("cities"))

tree.heading("#0",text="State")
tree.heading("cities",text="City")

tree.column("cities",anchor=CENTER)

for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.bind("<Double-1>",doubleClick)
tree.pack()

root.mainloop()