from tkinter import *
def btnClicked1():
    print("Command event handler, I like tkinter")
def btnClicked2(event):
    print("Bind event handler, I like tkinter")

root=Tk()
root.title("ch11_08")
root.geometry("300x180")

btn=Button(root,text="tkinter",command=btnClicked1)
btn.pack(anchor=W,padx=10,pady=10)
btn.bind("<Button-1>",btnClicked2,add="+")

root.mainloop()