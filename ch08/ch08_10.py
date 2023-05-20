from tkinter import *

root=Tk()
root.title("ch08_10")

tl=Toplevel()
tl.title("TopLevel")
tl.geometry("300x180")
Label(tl,text="I am a Toplevel").pack()

root.mainloop()