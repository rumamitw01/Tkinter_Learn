from tkinter import *

root=Tk()
root.title("ch17_15")
root.geometry("300x180")

text=Text(root)

for i in range(1,10):
    text.insert(END,str(i)+" Python GUI設計王者歸來\n")

text.mark_set("mark1","5.0")
text.mark_set("mark2","8.0")

text.tag_add("tag1","mark1","mark2")
text.tag_config("tag1",foreground="blue",background="lightyellow")
text.pack(fill=BOTH,expand=True)

root.mainloop()