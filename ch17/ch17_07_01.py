from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def familyChanged(event):
    f=Font(family=familyVar.get())
    text.configure(font=f)

root=Tk()
root.title("ch17_07_01")
root.geometry("300x180")

familyVar=StringVar()
familyFamily=("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family=Combobox(root,textvariable=familyVar,value=familyFamily)
family.bind("<<ComboboxSelected>>",familyChanged)
family.pack(pady=2)

text=Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()