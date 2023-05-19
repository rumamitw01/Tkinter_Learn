from tkinter import *

def msgShow():
    label["text"]="I love Python"
    label["bg"]="lightyellow"
    label["fg"]="blue"

root=Tk()
root.title("ch04_01")
label=Label(root)
btn=Button(root,text="列印訊息",command=msgShow)
label.pack()
btn.pack()

root.mainloop()