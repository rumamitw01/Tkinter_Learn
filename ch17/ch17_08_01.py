from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def familyChanged(event):
    f=Font(family=familyVar.get())
    text.configure(font=f)
def weightChanged(event):
    f=Font(weight=weightVar.get())
    text.configure(font=f)

root=Tk()
root.title("ch17_08_01")
root.geometry("300x180")

toolbar=Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

familyVar=StringVar()
familyFamily=("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family=Combobox(toolbar,textvariable=familyVar,value=familyFamily)
family.bind("<<ComboboxSelected>>",familyChanged)
family.pack(side=LEFT,pady=2)

weightVar=StringVar()
weightFamily=("normal","bold")
weightVar.set(weightFamily[0])
weight=Combobox(toolbar,textvariable=weightVar,value=weightFamily)
weight.bind("<<ComboboxSelected>>",weightChanged)
weight.pack(pady=3,side=LEFT)

text=Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()