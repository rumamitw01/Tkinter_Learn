from tkinter import *
from tkinter.font import Font

def familyChanged(event):
    f=Font(family=familyVar.get())
    text.configure(font=f)
def weightChanged(event):
    f=Font(weight=weightVar.get())
    text.configure(font=f)

root=Tk()
root.title("ch17_08")
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

text=Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()