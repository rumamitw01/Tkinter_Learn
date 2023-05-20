from tkinter import *
from tkinter.colorchooser import *
def bgUpdate():
    myColor=askcolor()
    print(type(myColor),myColor)
    root.config(bg=myColor[1])

root=Tk()
root.title("ch09_04_01")
root.geometry("360x240")

btn=Button(text="Select Color",command=bgUpdate)
btn.pack(pady=5)

root.mainloop()