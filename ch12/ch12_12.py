from tkinter import *
fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_12")
root.geometry("300x210")

lb=Listbox(root)
for fruit in fruits:
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1))

root.mainloop()