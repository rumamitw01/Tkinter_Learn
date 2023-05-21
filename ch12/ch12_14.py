from tkinter import *
def callback():
    indexes=lb.curselection()
    for index in indexes:
        print(lb.get(index))
fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_14")
root.geometry("300x250")

lb=Listbox(root,selectmode=MULTIPLE)
for fruit in fruits:
    lb.insert(END,fruit)
lb.pack(pady=5)
btn=Button(root,text="Print",command=callback)
btn.pack(pady=5)

root.mainloop()