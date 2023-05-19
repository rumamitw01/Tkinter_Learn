from tkinter import *

def yellow():
    root.config(bg="yellow")
def blue():
    root.config(bg="blue")

root=Tk()
root.title("ch04_05")
root.geometry("300x200")
exitbtn=Button(root,text="Exit",command=root.destroy)
bluebtn=Button(root,text="Blue",command=blue)
yellowbtn=Button(root,text="Yellow",command=yellow)
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()