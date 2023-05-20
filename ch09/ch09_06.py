from tkinter import *

root=Tk()
root.title("ch09_06")
root.geometry("300x100")
spin=Spinbox(root,from_=10,to=30,increment=2)
spin.pack(pady=20)

root.mainloop()