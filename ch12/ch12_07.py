from tkinter import *
fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_07")
root.geometry("300x210")

lb=Listbox(root,selectmode=EXTENDED)
for fruit in fruits:
    lb.insert(END,fruit)
lb.pack(pady=10)
print("items數字：",lb.size())

root.mainloop()