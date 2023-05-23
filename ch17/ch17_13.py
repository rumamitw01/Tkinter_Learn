from tkinter import *

root=Tk()
root.title("ch17_13")
root.geometry("300x180")

text=Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song\n")
text.insert((1.14),"夢醒時分 ")

root.mainloop()