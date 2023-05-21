from tkinter import *
def getIndex(event):
    lb.index=lb.nearest(event.y)

def dragJob(event):
    newIndex=lb.nearest(event.y)
    if newIndex<lb.index:
        x=lb.get(newIndex)
        lb.delete(newIndex)
        lb.insert(newIndex+1,x)
        lb.index=newIndex
    if newIndex>lb.index:
        x=lb.get(newIndex)
        lb.delete(newIndex)
        lb.insert(newIndex-1,x)
        lb.index=newIndex

fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_21")

lb=Listbox(root)
for fruit in fruits:
    lb.insert(END,fruit)
    lb.bind("<Button-1>",getIndex)
    lb.bind("<B1-Motion>",dragJob)
lb.pack(padx=10,pady=10)

root.mainloop()