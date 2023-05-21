from tkinter import *
def itemSelected(event):
    obj=event.widget
    indexes=obj.curselection()
    for index in indexes:
        print(obj.get(index))
    print("----------")
fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_18")
root.geometry("300x250")

var=StringVar()
lab=Label(root,text="",textvariable=var)
lab.pack(pady=5)
lb=Listbox(root,selectmode=EXTENDED)
for fruit in fruits:
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected)
lb.pack(pady=10)

root.mainloop()