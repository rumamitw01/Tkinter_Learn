from tkinter import *

def printIndex():
    print("INSERT:",text.index(INSERT))
    print("CURRENT:",text.index(CURRENT))
    print("END:",text.index(END))

root=Tk()
root.title("ch17_12")
root.geometry("300x180")

btn=Button(root,text="Print Index",command=printIndex)
btn.pack(pady=3)

text=Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song\n")
text.insert(END,"夢醒時分")

root.mainloop()