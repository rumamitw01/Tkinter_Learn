from tkinter import *

root=Tk()
root.title("ch12_22")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

lb=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(1,51):
    lb.insert(END,"Line "+str(i))
lb.pack(side=LEFT,fill=BOTH,expand=True)

scrollbar.config(command=lb.yview)

root.mainloop()