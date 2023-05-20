from tkinter import *
def key(event):
    print("按了"+repr(event.char)+"鍵")

root=Tk()
root.title("ch11_05")

root.bind("<Key>",key)

root.mainloop()