from tkinter import *

def spellingCheck():
    text.tag_remove("spellErr","1.0",END)
    textwords=text.get("1.0",END).split()
    print("字典內容\n",textwords)
    startChar=("(")
    endChar=(".",",","?",")","!",":",";")
    start="1.0"
    for word in textwords:
        if word[0] in startChar:
            word=word[1:]
        if word[-1] in endChar:
            word=word[:-1]
        if word not in dicts and word.lower() not in dicts:
            print("error",word)
            pos=text.search(word,start,END)
            text.tag_add("spellErr",pos,f"{pos}+{len(word)}c")
            pos=f"{pos}+{len(word)}c"

def clrText():
    text.tag_remove("spellErr","1.0",END)

root=Tk()
root.title("ch17_22")
root.geometry("300x180")

toolbar=Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

chkBtn=Button(toolbar,text="拼字檢查",command=spellingCheck)
chkBtn.pack(side=LEFT,padx=5,pady=5)

clrBtn=Button(toolbar,text="清除",command=clrText)
clrBtn.pack(side=LEFT,padx=5,pady=5)

text=Text(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

text.tag_configure("spellErr",foreground="red")
with open("myDict.txt","r") as dictObj:
    dicts=dictObj.read().split("\n")

root.mainloop()