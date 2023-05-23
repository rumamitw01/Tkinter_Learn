from tkinter import *

root=Tk()
root.title("ch17_05")

xscrollbar=Scrollbar(root,orient=HORIZONTAL)
yscrollbar=Scrollbar(root)
text=Text(root,height=5,width=30,wrap="none")
xscrollbar.pack(side=BOTTOM,fill=X)
yscrollbar.pack(side=RIGHT,fill=Y)
text.pack()
xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)
text.config(xscrollcommand=xscrollbar.set)
text.config(yscrollcommand=yscrollbar.set)

str="""Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate."""
text.insert(END,str)

root.mainloop()