from tkinter import *

def printInfo():
    selection=""
    for i in checkboxes:
        if checkboxes[i].get()==True:
            selection=selection+sports[i]+" "
        else:
            selection+=""
    print(selection)

root=Tk()
root.title("ch07_08")

lab=Label(root,text="請選擇喜歡的運動",fg="blue",bg="lightyellow",width=30)
lab.grid(row=0)

sports={0:"美式足球",1:"棒球",2:"籃球",3:"網球"}
checkboxes={}
for i in range(len(sports)):
    checkboxes[i]=BooleanVar()
    Checkbutton(root,text=sports[i],variable=checkboxes[i]).grid(row=i+1,sticky=W)

btn=Button(root,text="確定",width=10,command=printInfo)
btn.grid(row=i+2)

root.mainloop()