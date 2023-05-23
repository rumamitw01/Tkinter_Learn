from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):
    f=Font(size=sizeVar.get())
    text.tag_config(SEL,font=f)

root=Tk()
root.title("ch17_17")
root.geometry("300x180")

toolbar=Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

sizeVar=IntVar()
size=Combobox(toolbar,textvariable=sizeVar)
sizeFamily=[x for x in range(8,31)]
size["value"]=sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack()

text=Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n","a")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")
text.focus_set()

text.tag_config("a",foreground="blue",justify=CENTER,underline=True)

root.mainloop()