from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("ch18_13")
reverseFlag=False

stateCity={"伊利諾州":"芝加哥","加州":"洛杉磯",
           "德州":"休士頓","華盛頓州":"西雅圖",
           "江蘇":"南京","山東":"青島",
           "廣東":"廣州","福建":"廈門",
           "密西西比州":"牛津","肯塔基州":"萊辛頓",
           "佛羅里達州":"邁阿密","印第安納州":"西拉法葉"}

tree=Treeview(root,columns=("cities"))
yscrollbar=Scrollbar(root)
yscrollbar.pack(side=RIGHT,fill=Y)
tree.pack()
yscrollbar.config(command=tree.yview)
tree.configure(yscrollcommand=yscrollbar.set)

tree.heading("#0",text="State")
tree.heading("cities",text="City")

tree.column("cities",anchor=CENTER)

for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])

root.mainloop()