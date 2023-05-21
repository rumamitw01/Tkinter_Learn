from tkinter import *
def callback():
    print(lb.selection_includes(3))
fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_15")
root.geometry("300x250")

lb=Listbox(root,selectmode=MULTIPLE)
for fruit in fruits:
    lb.insert(END,fruit)
lb.pack(pady=5)
btn=Button(root,text="Check",command=callback)
btn.pack(pady=5)

root.mainloop()