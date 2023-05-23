from tkinter import *

def saveFile():
    textContent=text.get("1.0",END)
    filename="ch17_23.txt"
    with open(filename,"w") as output:
        output.write(textContent)
        root.title(filename)

root=Tk()
root.title("Untitled")
root.geometry("300x180")

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Exit",command=root.destroy)
root.config(menu=menubar)

text=Text(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop()