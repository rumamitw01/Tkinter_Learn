from tkinter import *

root=Tk()
root.title("ch12_02")
root.geometry("300x210")

lb=Listbox(root)
lb.insert(END,"Banana")
lb.insert(END,"Watermelon")
lb.insert(END,"Pineapple")
lb.pack(pady=10)

root.mainloop()