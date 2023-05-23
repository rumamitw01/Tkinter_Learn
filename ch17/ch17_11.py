from tkinter import *

def selectedText():
    try:
        selText=text.get(SEL_FIRST,SEL_LAST)
        print("選取文字：",selText)
        print("selectionstart:",text.index(SEL_FIRST))
        print("selectionend:",text.index(SEL_LAST))
    except TclError:
        print("沒有選取文字")

root=Tk()
root.title("ch17_11")
root.geometry("300x180")

btn=Button(root,text="Print Selection",command=selectedText)
btn.pack(pady=3)

text=Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song")

root.mainloop()