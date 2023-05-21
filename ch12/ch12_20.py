from tkinter import *
def itemSorted():
    if var.get()==True:
        revBool=True
    else:
        revBool=False
    listTmp=list(lb.get(0,END))
    sortedList=sorted(listTmp,reverse=revBool)
    lb.delete(0,END)
    for item in sortedList:
        lb.insert(END,item)

fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_20")

lb=Listbox(root)
for fruit in fruits:
    lb.insert(END,fruit)
lb.pack(padx=10,pady=5)

btn=Button(root,text="排序",command=itemSorted)
btn.pack(side=LEFT,padx=10,pady=5)

var=BooleanVar()
cb=Checkbutton(root,text="大到小排序",variable=var)
cb.pack(side=LEFT)

root.mainloop()