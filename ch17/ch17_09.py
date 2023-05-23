from tkinter import *
from tkinter.font import Font
import tkinter.ttk as ttk

def familyChanged(event):
    f=Font(family=familyVar.get())
    text.configure(font=f)
def weightChanged(event):
    f=Font(weight=weightVar.get())
    text.configure(font=f)
def sizeSelected(event):
    f=Font(size=sizeVar.get())
    text.configure(font=f)

root=Tk()
root.title("ch17_09")
root.geometry("300x180")

toolbar=Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

familyVar=StringVar()
familyFamily=("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family=OptionMenu(toolbar,familyVar,*familyFamily,command=familyChanged)
family.pack(side=LEFT,pady=2)

weightVar=StringVar()
weightFamily=("normal","bold")
weightVar.set(weightFamily[0])
weight=OptionMenu(toolbar,weightVar,*weightFamily,command=weightChanged)
weight.pack(pady=3,side=LEFT)

sizeVar=IntVar()
size=ttk.Combobox(toolbar,textvariable=sizeVar)
sizeFamily=[x for x in range(8,31)]
size["value"]=sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack(side=LEFT)

text=Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()