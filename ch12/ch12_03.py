from tkinter import *
fruits=["Banana","Watermelon","Pineapple","Orange","Grapes","Mango"]

root=Tk()
root.title("ch12_03")
root.geometry("300x210")

lb=Listbox(root)
for fruit in fruits:
    lb.insert(END,fruit)
lb.pack(pady=10)

root.mainloop()