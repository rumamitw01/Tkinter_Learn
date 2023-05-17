from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("ch02_19_01")
root.geometry("680x400")

image=Image.open("yellowstone.jpg")
yellowstone=ImageTk.PhotoImage(image)
label=Label(root,image=yellowstone)
label.pack()

root.mainloop()