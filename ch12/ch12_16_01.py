from tkinter import *
def itemSelected(event):
    index=lb.curselection()
    var.set(lb.get(index))
fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_16_01")
root.geometry("300x250")

var=StringVar()
lab=Label(root,text="",textvariable=var)
lab.pack(pady=5)
lb=Listbox(root)
for fruit in fruits:
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected)
lb.pack(pady=10)

root.mainloop()