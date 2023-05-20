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
root.title("ch08_08")
root.geometry("400x220")

labFrame=LabelFrame(root,text="請選擇喜歡的運動")
sports={0:"美式足球",1:"棒球",2:"籃球",3:"網球"}
checkboxes={}
for i in range(len(sports)):
    checkboxes[i]=BooleanVar()
    Checkbutton(labFrame,text=sports[i],variable=checkboxes[i]).grid(row=i+1,sticky=W)
labFrame.pack(ipadx=5,ipady=5,pady=10)

btn=Button(root,text="確定",width=10,command=printInfo)
btn.pack()

root.mainloop()