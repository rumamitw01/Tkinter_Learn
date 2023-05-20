from tkinter import *

root=Tk()
root.title("ch08_03")

frameUpper=Frame(root,bg="lightyellow")
frameUpper.pack()
btnRed=Button(frameUpper,text="Red",fg="red")
btnRed.pack(side=LEFT,padx=5,pady=5)
btnGreen=Button(frameUpper,text="Green",fg="green")
btnGreen.pack(side=LEFT,padx=5,pady=5)
btnBlue=Button(frameUpper,text="Blue",fg="blue")
btnBlue.pack(side=LEFT,padx=5,pady=5)

frameLower=Frame(root,bg="lightblue")
frameLower.pack()
btnPurple=Button(frameLower,text="Purple",fg="purple")
btnPurple.pack(side=LEFT,padx=5,pady=5)

root.mainloop()