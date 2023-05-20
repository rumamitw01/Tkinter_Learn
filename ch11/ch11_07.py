from tkinter import *
def buttonClicked(event):
    print("I like tkinter")

def toggle(onoff):
    if var.get()==True:
        onoff.bind("<Button-1>",buttonClicked)
    else:
        onoff.unbind("<Button-1>")

root=Tk()
root.title("ch11_07")
root.geometry("300x180")

btn=Button(root,text="tkinter")
btn.pack(anchor=W,padx=10,pady=10)

var=BooleanVar()
cbtn=Checkbutton(root,text="bind/unbind",variable=var,command=lambda:toggle(btn))
cbtn.pack(anchor=W,padx=10)

root.mainloop()