from tkinter import *
from tkinter.ttk import *
def treeview_sortColumn(col):
    global reverseFlag
    lst=[(tree.set(st,col),st) for st in tree.get_children("")]
    print(lst)
    lst.sort(reverse=reverseFlag)
    print(lst)
    for index,item in enumerate(lst):
        tree.move(item[1],"",index)
    reverseFlag=not reverseFlag
root=Tk()
root.title("ch18_14")
reverseFlag=False

myStates={"Illinois","California","Texas","Washington","Jiangsu","Shandong","Guangdong","Fujian","Mississippi","Kentucky","Florida","Indiana"}

tree=Treeview(root,columns=("states"),show="headings")
yscrollbar=Scrollbar(root)
yscrollbar.pack(side=RIGHT,fill=Y)
tree.pack()
yscrollbar.config(command=tree.yview)
tree.configure(yscrollcommand=yscrollbar.set)

tree.heading("states",text="State")

for state in myStates:
    tree.insert("",index=END,values=(state,))
tree.heading("#1",text="State",command=lambda c="states": treeview_sortColumn(c))

root.mainloop()